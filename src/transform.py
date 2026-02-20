"""Transformation layer for the sales ETL pipeline."""

from __future__ import annotations

import logging

import pandas as pd

logger = logging.getLogger(__name__)

REQUIRED_COLUMNS = [
    "order_id",
    "order_date",
    "customer_id",
    "customer_name",
    "product_id",
    "product_name",
    "category",
    "quantity",
    "unit_price",
    "discount",
    "region",
    "sales_rep",
]


def _validate_required_columns(df: pd.DataFrame) -> None:
    """Validate that expected columns are present in the dataset."""
    missing = [column for column in REQUIRED_COLUMNS if column not in df.columns]
    if missing:
        raise ValueError(f"Missing required columns: {missing}")


def transform_sales_data(raw_df: pd.DataFrame) -> pd.DataFrame:
    """Clean and enrich sales data for loading into PostgreSQL.

    Steps:
      - Validate schema
      - Remove duplicate orders
      - Parse date fields
      - Cast numeric columns and sanitize invalid records
      - Add gross and net sales amounts
    """
    logger.info("Starting transformation for %s records", len(raw_df))

    try:
        _validate_required_columns(raw_df)

        df = raw_df.copy()
        initial_count = len(df)

        # Remove duplicate order records, retaining latest occurrence.
        df = df.drop_duplicates(subset=["order_id"], keep="last")

        # Normalize text fields.
        text_columns = [
            "customer_id",
            "customer_name",
            "product_id",
            "product_name",
            "category",
            "region",
            "sales_rep",
        ]
        for column in text_columns:
            df[column] = df[column].astype(str).str.strip()

        # Parse and validate date field.
        df["order_date"] = pd.to_datetime(df["order_date"], errors="coerce")

        # Convert numeric fields.
        numeric_columns = ["quantity", "unit_price", "discount"]
        for column in numeric_columns:
            df[column] = pd.to_numeric(df[column], errors="coerce")

        # Keep only valid business records.
        df = df.dropna(subset=["order_id", "order_date", "quantity", "unit_price", "discount"])
        df = df[df["quantity"] > 0]
        df = df[df["unit_price"] >= 0]
        df = df[(df["discount"] >= 0) & (df["discount"] <= 1)]

        # Standardize key types.
        df["order_id"] = df["order_id"].astype("int64")
        df["quantity"] = df["quantity"].astype("int64")
        df["order_date"] = df["order_date"].dt.date

        # Add derived measures.
        df["gross_amount"] = (df["quantity"] * df["unit_price"]).round(2)
        df["net_amount"] = (df["gross_amount"] * (1 - df["discount"])).round(2)

        removed_records = initial_count - len(df)
        logger.info("Transformation successful. Final rows: %s (removed: %s)", len(df), removed_records)
        return df
    except Exception:
        logger.exception("Transformation failed")
        raise

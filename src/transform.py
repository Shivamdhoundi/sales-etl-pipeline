"""Transform step for sales ETL pipeline."""

from __future__ import annotations

import pandas as pd


def transform_sales_data(df: pd.DataFrame) -> pd.DataFrame:
    """Clean and enrich raw sales dataframe."""
    transformed = df.copy()

    transformed["order_date"] = pd.to_datetime(transformed["order_date"], errors="coerce")
    transformed = transformed.dropna(subset=["order_id", "order_date", "customer_id", "product_id"])

    transformed["quantity"] = pd.to_numeric(transformed["quantity"], errors="coerce").fillna(0).astype(int)
    transformed["unit_price"] = pd.to_numeric(transformed["unit_price"], errors="coerce").fillna(0.0)

    transformed = transformed[transformed["quantity"] > 0]
    transformed = transformed[transformed["unit_price"] >= 0]

    transformed["gross_sales"] = transformed["quantity"] * transformed["unit_price"]
    transformed["order_month"] = transformed["order_date"].dt.to_period("M").astype(str)

    transformed["region"] = transformed["region"].fillna("UNKNOWN").str.strip().str.upper()

    transformed = transformed.drop_duplicates(subset=["order_id", "product_id"], keep="last")

    return transformed.reset_index(drop=True)

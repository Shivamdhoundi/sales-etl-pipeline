from typing import Tuple

import pandas as pd


def transform_sales_data(raw_df: pd.DataFrame) -> Tuple[pd.DataFrame, pd.DataFrame]:
    """
    Clean and enrich raw sales data.

    Returns a tuple of:
      1) cleaned row-level sales records
      2) daily summary by date/region/product
    """
    df = raw_df.copy()

    df["order_date"] = pd.to_datetime(df["order_date"], errors="coerce")
    df["quantity"] = pd.to_numeric(df["quantity"], errors="coerce")
    df["unit_price"] = pd.to_numeric(df["unit_price"], errors="coerce")

    df = df.dropna(subset=["order_date", "quantity", "unit_price"])
    df = df[(df["quantity"] > 0) & (df["unit_price"] >= 0)]

    df["total_amount"] = (df["quantity"] * df["unit_price"]).round(2)
    df["order_date"] = df["order_date"].dt.date

    cleaned_sales = df[
        [
            "order_id",
            "order_date",
            "customer_id",
            "product",
            "region",
            "quantity",
            "unit_price",
            "total_amount",
        ]
    ].reset_index(drop=True)

    sales_summary = (
        cleaned_sales.groupby(["order_date", "region", "product"], as_index=False)
        .agg(
            total_orders=("order_id", "nunique"),
            total_units=("quantity", "sum"),
            total_revenue=("total_amount", "sum"),
        )
        .sort_values(["order_date", "region", "product"])
        .reset_index(drop=True)
    )

    sales_summary["total_revenue"] = sales_summary["total_revenue"].round(2)

    return cleaned_sales, sales_summary

"""Extract step for sales ETL pipeline."""

from __future__ import annotations

import pandas as pd


def extract_sales_data(file_path: str) -> pd.DataFrame:
    """Extract sales records from CSV file.

    Expected columns:
      - order_id
      - order_date
      - customer_id
      - product_id
      - quantity
      - unit_price
      - region
    """
    return pd.read_csv(file_path)

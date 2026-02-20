from pathlib import Path
from typing import Union

import pandas as pd


REQUIRED_COLUMNS = {
    "order_id",
    "order_date",
    "customer_id",
    "product",
    "region",
    "quantity",
    "unit_price",
}


def extract_sales_data(csv_path: Union[str, Path]) -> pd.DataFrame:
    """Read raw sales data from a CSV file and validate required columns."""
    csv_path = Path(csv_path)
    if not csv_path.exists():
        raise FileNotFoundError(f"Sales data file not found: {csv_path}")

    df = pd.read_csv(csv_path)
    missing_columns = REQUIRED_COLUMNS.difference(df.columns)
    if missing_columns:
        missing = ", ".join(sorted(missing_columns))
        raise ValueError(f"Missing required columns in source data: {missing}")

    return df

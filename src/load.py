"""Load step for sales ETL pipeline."""

from __future__ import annotations

import pandas as pd
from sqlalchemy import create_engine


def load_sales_data(df: pd.DataFrame, sqlalchemy_uri: str, table_name: str = "fact_sales") -> None:
    """Load transformed dataframe into PostgreSQL table."""
    engine = create_engine(sqlalchemy_uri)
    with engine.begin() as connection:
        df.to_sql(table_name, con=connection, if_exists="append", index=False, method="multi")

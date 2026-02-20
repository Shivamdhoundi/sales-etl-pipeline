from pathlib import Path
from typing import Optional

import pandas as pd
from sqlalchemy import create_engine, text
from sqlalchemy.engine import Engine


def get_engine(database_url: Optional[str] = None) -> Engine:
    """Create a SQLAlchemy engine for the configured database URL."""
    database_url = database_url or "postgresql+psycopg2://postgres:postgres@localhost:5432/sales_db"
    return create_engine(database_url)


def create_tables(engine: Engine, sql_file: str = "sql/create_tables.sql") -> None:
    """Create destination tables using SQL statements from a file."""
    sql_path = Path(sql_file)
    if not sql_path.exists():
        raise FileNotFoundError(f"SQL file not found: {sql_path}")

    sql_script = sql_path.read_text(encoding="utf-8")
    statements = [stmt.strip() for stmt in sql_script.split(";") if stmt.strip()]

    with engine.begin() as conn:
        for statement in statements:
            conn.execute(text(statement))


def load_dataframe(df: pd.DataFrame, table_name: str, engine: Engine) -> None:
    """Append DataFrame records into a destination table."""
    df.to_sql(table_name, engine, if_exists="append", index=False)


def load_sales_data(cleaned_sales: pd.DataFrame, sales_summary: pd.DataFrame, engine: Engine) -> None:
    """Load transformed sales datasets into database tables."""
    load_dataframe(cleaned_sales, "sales", engine)
    load_dataframe(sales_summary, "sales_summary", engine)

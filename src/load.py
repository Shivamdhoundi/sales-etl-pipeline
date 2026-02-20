"""Load layer for persisting transformed sales data into PostgreSQL."""

from __future__ import annotations

import logging

import pandas as pd
from sqlalchemy import create_engine, text
from sqlalchemy.engine import Engine

logger = logging.getLogger(__name__)


def create_db_engine(db_url: str) -> Engine:
    """Create and validate a SQLAlchemy engine for PostgreSQL."""
    try:
        engine = create_engine(db_url)
        with engine.connect() as connection:
            connection.execute(text("SELECT 1"))
        logger.info("Database connection established successfully")
        return engine
    except Exception:
        logger.exception("Failed to create database engine")
        raise


def load_sales_data(df: pd.DataFrame, db_url: str, table_name: str = "sales_data") -> None:
    """Load transformed records into PostgreSQL.

    Data is inserted in append mode and respects the target schema defined
    in sql/create_sales_table.sql.
    """
    logger.info("Starting load for %s records into table '%s'", len(df), table_name)

    if df.empty:
        logger.warning("No records to load. Skipping database write.")
        return

    try:
        engine = create_db_engine(db_url)
        df.to_sql(name=table_name, con=engine, if_exists="append", index=False, method="multi", chunksize=1000)
        logger.info("Load successful. Inserted %s rows into table '%s'", len(df), table_name)
    except Exception:
        logger.exception("Load failed")
        raise

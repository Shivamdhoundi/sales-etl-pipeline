"""Orchestrator for the sales ETL pipeline."""

from __future__ import annotations

import logging
import os
import sys

from dotenv import load_dotenv

from extract import extract_sales_data
from load import load_sales_data
from transform import transform_sales_data


def configure_logging() -> None:
    """Configure a production-friendly logging format."""
    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s | %(levelname)s | %(name)s | %(message)s",
    )


def run_pipeline() -> None:
    """Execute ETL flow: extract -> transform -> load."""
    load_dotenv()
    configure_logging()
    logger = logging.getLogger(__name__)

    source_file = os.getenv("SOURCE_CSV_PATH", "data/sample_sales.csv")
    db_url = os.getenv("DATABASE_URL")

    if not db_url:
        raise EnvironmentError("DATABASE_URL is not set. Please configure it in your environment.")

    logger.info("Pipeline execution started")

    raw_df = extract_sales_data(source_file)
    transformed_df = transform_sales_data(raw_df)
    load_sales_data(transformed_df, db_url=db_url)

    logger.info("Pipeline execution completed successfully")


if __name__ == "__main__":
    try:
        run_pipeline()
    except Exception as exc:  # Final catch to ensure clear process-level failure logging.
        logging.getLogger(__name__).exception("Pipeline execution failed: %s", exc)
        sys.exit(1)

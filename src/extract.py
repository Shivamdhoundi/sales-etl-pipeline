"""Extraction layer for the sales ETL pipeline."""

from __future__ import annotations

import logging
from pathlib import Path

import pandas as pd

logger = logging.getLogger(__name__)


def extract_sales_data(file_path: str | Path) -> pd.DataFrame:
    """Read raw sales CSV data into a DataFrame.

    Args:
        file_path: Path to the source CSV file.

    Returns:
        A pandas DataFrame containing raw sales records.

    Raises:
        FileNotFoundError: If the source file does not exist.
        ValueError: If the file is empty.
        Exception: Re-raised for any unexpected extraction failure.
    """
    file_path = Path(file_path)
    logger.info("Starting extraction from: %s", file_path)

    if not file_path.exists():
        msg = f"Source file not found: {file_path}"
        logger.error(msg)
        raise FileNotFoundError(msg)

    try:
        dataframe = pd.read_csv(file_path)
        if dataframe.empty:
            msg = f"Source file is empty: {file_path}"
            logger.error(msg)
            raise ValueError(msg)

        logger.info("Extraction successful. Rows: %s, Columns: %s", *dataframe.shape)
        return dataframe
    except Exception:
        logger.exception("Extraction failed for file: %s", file_path)
        raise

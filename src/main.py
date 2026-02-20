"""Entrypoint for the sales ETL pipeline."""

from __future__ import annotations

from src.config import Settings
from src.extract import extract_sales_data
from src.load import load_sales_data
from src.transform import transform_sales_data


def run_pipeline() -> None:
    """Run extract, transform, and load steps."""
    settings = Settings()

    raw_df = extract_sales_data(settings.raw_data_path)
    transformed_df = transform_sales_data(raw_df)

    load_sales_data(transformed_df, settings.sqlalchemy_uri)

    print(
        "Pipeline completed successfully. "
        f"Extracted={len(raw_df)} rows, Loaded={len(transformed_df)} rows."
    )


if __name__ == "__main__":
    run_pipeline()

import os
from pathlib import Path

from extract import extract_sales_data
from load import create_tables, get_engine, load_sales_data
from transform import transform_sales_data


def run_etl(
    source_csv: str = "data/sales_raw.csv",
    sql_file: str = "sql/create_tables.sql",
) -> None:
    raw_df = extract_sales_data(source_csv)
    cleaned_sales, sales_summary = transform_sales_data(raw_df)

    database_url = os.getenv("DATABASE_URL")
    engine = get_engine(database_url)

    create_tables(engine, sql_file)
    load_sales_data(cleaned_sales, sales_summary, engine)

    print(f"Loaded {len(cleaned_sales)} sales records into 'sales'.")
    print(f"Loaded {len(sales_summary)} summary records into 'sales_summary'.")


if __name__ == "__main__":
    project_root = Path(__file__).resolve().parent.parent
    os.chdir(project_root)
    run_etl()

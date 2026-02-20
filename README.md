# Sales Data ETL Pipeline

End-to-end Sales Data ETL Pipeline using Python and PostgreSQL.

## Project Structure

```text
sales-etl-pipeline/
├── .env.example
├── .gitignore
├── docker-compose.yml
├── Makefile
├── requirements.txt
├── README.md
├── data/
│   └── raw/
│       └── sales_data.csv
├── sql/
│   └── init.sql
├── src/
│   ├── __init__.py
│   ├── config.py
│   ├── extract.py
│   ├── load.py
│   ├── main.py
│   └── transform.py
└── tests/
    └── test_transform.py
```

## Features

- **Extract** sales records from a CSV file.
- **Transform** data with cleaning, validation, and enrichment logic.
- **Load** transformed records into a PostgreSQL `fact_sales` table.
- Includes test coverage for transformation behavior.

## Quick Start

1. Create and activate a virtual environment.
2. Install dependencies.
3. Start PostgreSQL via Docker.
4. Copy environment variables and run the pipeline.

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
cp .env.example .env
docker compose up -d
python -m src.main
```

## Data Flow

1. `src.extract.extract_sales_data`: reads CSV raw sales data.
2. `src.transform.transform_sales_data`: converts types, drops invalid rows, standardizes regions, and computes metrics.
3. `src.load.load_sales_data`: appends results into PostgreSQL table `fact_sales`.

## Running Tests

```bash
pytest -q
```

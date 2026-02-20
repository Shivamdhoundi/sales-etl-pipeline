# Sales Data ETL Pipeline

A production-ready Python ETL pipeline project that extracts sales records from CSV, transforms and cleans the data using Pandas, and loads curated records into PostgreSQL.

## Project Structure

```text
sales-etl-pipeline/
├── data/
│   └── sample_sales.csv
├── sql/
│   └── create_sales_table.sql
├── src/
│   ├── extract.py
│   ├── transform.py
│   ├── load.py
│   └── main.py
├── requirements.txt
└── README.md
```

## Features

- Modular ETL architecture (`extract`, `transform`, `load`, `main` orchestrator)
- Data cleaning and validation with Pandas
- PostgreSQL loading using SQLAlchemy + psycopg2
- Structured logging and robust error handling
- Sample dataset and SQL schema script for quick local setup

## Setup Instructions

### 1) Clone repository and create a virtual environment

```bash
git clone <your-repo-url>
cd sales-etl-pipeline
python -m venv .venv
source .venv/bin/activate  # Windows: .venv\Scripts\activate
```

### 2) Install dependencies

```bash
pip install -r requirements.txt
```

### 3) Create PostgreSQL table

Run the SQL script:

```bash
psql "$DATABASE_URL" -f sql/create_sales_table.sql
```

### 4) Configure environment variables

Set environment variables before running the pipeline:

```bash
export DATABASE_URL="postgresql+psycopg2://username:password@localhost:5432/sales_db"
export SOURCE_CSV_PATH="data/sample_sales.csv"  # optional
```

You can also store values in a `.env` file:

```env
DATABASE_URL=postgresql+psycopg2://username:password@localhost:5432/sales_db
SOURCE_CSV_PATH=data/sample_sales.csv
```

### 5) Run the ETL pipeline

```bash
python src/main.py
```

## ETL Flow

1. **Extract**: Reads CSV source data into a DataFrame.
2. **Transform**: Cleans nulls/types, validates records, deduplicates, and adds `gross_amount` + `net_amount`.
3. **Load**: Appends transformed rows into PostgreSQL table `sales_data`.

## Notes for Portfolio Presentation

- Keep logs visible in your demo to highlight production readiness.
- Showcase SQL table design and the validation rules in `transform.py`.
- Consider extending with unit tests, Docker, and orchestration (Airflow/Prefect) for advanced demonstrations.

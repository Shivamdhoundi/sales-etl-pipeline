"""Configuration utilities for ETL pipeline."""

from __future__ import annotations

import os
from dataclasses import dataclass

from dotenv import load_dotenv


load_dotenv()


@dataclass(frozen=True)
class Settings:
    """Application settings loaded from environment variables."""

    db_host: str = os.getenv("DB_HOST", "localhost")
    db_port: int = int(os.getenv("DB_PORT", "5432"))
    db_name: str = os.getenv("DB_NAME", "sales")
    db_user: str = os.getenv("DB_USER", "sales_user")
    db_password: str = os.getenv("DB_PASSWORD", "sales_password")
    raw_data_path: str = os.getenv("RAW_DATA_PATH", "data/raw/sales_data.csv")

    @property
    def sqlalchemy_uri(self) -> str:
        """Build SQLAlchemy PostgreSQL URI."""
        return (
            "postgresql+psycopg2://"
            f"{self.db_user}:{self.db_password}@{self.db_host}:{self.db_port}/{self.db_name}"
        )

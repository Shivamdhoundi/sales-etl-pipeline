import pandas as pd

from src.transform import transform_sales_data


def test_transform_sales_data_filters_invalid_rows_and_adds_columns():
    raw = pd.DataFrame(
        [
            {
                "order_id": "1",
                "order_date": "2025-01-01",
                "customer_id": "C1",
                "product_id": "P1",
                "quantity": "2",
                "unit_price": "10.5",
                "region": "north",
            },
            {
                "order_id": "2",
                "order_date": "bad-date",
                "customer_id": "C2",
                "product_id": "P2",
                "quantity": "1",
                "unit_price": "20",
                "region": "west",
            },
            {
                "order_id": "3",
                "order_date": "2025-01-02",
                "customer_id": "C3",
                "product_id": "P3",
                "quantity": "0",
                "unit_price": "10",
                "region": None,
            },
        ]
    )

    transformed = transform_sales_data(raw)

    assert len(transformed) == 1
    row = transformed.iloc[0]
    assert row["gross_sales"] == 21.0
    assert row["order_month"] == "2025-01"
    assert row["region"] == "NORTH"

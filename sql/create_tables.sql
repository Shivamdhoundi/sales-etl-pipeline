CREATE TABLE IF NOT EXISTS sales (
    id SERIAL PRIMARY KEY,
    order_id VARCHAR(50) NOT NULL,
    order_date DATE NOT NULL,
    customer_id VARCHAR(50) NOT NULL,
    product VARCHAR(100) NOT NULL,
    region VARCHAR(50) NOT NULL,
    quantity INTEGER NOT NULL,
    unit_price NUMERIC(10,2) NOT NULL,
    total_amount NUMERIC(12,2) NOT NULL
);

CREATE TABLE IF NOT EXISTS sales_summary (
    id SERIAL PRIMARY KEY,
    order_date DATE NOT NULL,
    region VARCHAR(50) NOT NULL,
    product VARCHAR(100) NOT NULL,
    total_orders INTEGER NOT NULL,
    total_units INTEGER NOT NULL,
    total_revenue NUMERIC(12,2) NOT NULL
);

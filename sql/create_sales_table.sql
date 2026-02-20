-- SQL script to create the target sales table in PostgreSQL.
CREATE TABLE IF NOT EXISTS sales_data (
    order_id BIGINT PRIMARY KEY,
    order_date DATE NOT NULL,
    customer_id VARCHAR(50) NOT NULL,
    customer_name VARCHAR(255) NOT NULL,
    product_id VARCHAR(50) NOT NULL,
    product_name VARCHAR(255) NOT NULL,
    category VARCHAR(100) NOT NULL,
    quantity INTEGER NOT NULL CHECK (quantity > 0),
    unit_price NUMERIC(12,2) NOT NULL CHECK (unit_price >= 0),
    discount NUMERIC(5,2) NOT NULL DEFAULT 0 CHECK (discount >= 0 AND discount <= 1),
    gross_amount NUMERIC(14,2) NOT NULL,
    net_amount NUMERIC(14,2) NOT NULL,
    region VARCHAR(100) NOT NULL,
    sales_rep VARCHAR(255) NOT NULL,
    created_at TIMESTAMP WITHOUT TIME ZONE NOT NULL DEFAULT NOW()
);

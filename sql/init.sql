CREATE TABLE IF NOT EXISTS fact_sales (
    order_id VARCHAR(50) NOT NULL,
    order_date TIMESTAMP NOT NULL,
    customer_id VARCHAR(50) NOT NULL,
    product_id VARCHAR(50) NOT NULL,
    quantity INTEGER NOT NULL,
    unit_price NUMERIC(12,2) NOT NULL,
    region VARCHAR(50) NOT NULL,
    gross_sales NUMERIC(14,2) NOT NULL,
    order_month VARCHAR(7) NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE INDEX IF NOT EXISTS idx_fact_sales_order_date ON fact_sales(order_date);
CREATE INDEX IF NOT EXISTS idx_fact_sales_region ON fact_sales(region);

CREATE OR REPLACE VIEW monthly_sales AS
SELECT 
    order_year,
    order_month,
    ROUND(SUM(sales),2) AS monthly_revenue,
    ROUND(SUM(profit),2) AS monthly_profit
FROM orders
GROUP BY order_year, order_month
ORDER BY order_year, order_month;

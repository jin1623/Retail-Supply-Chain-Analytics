-- Total Revenue & Profit
SELECT 
    ROUND(SUM(sales),2) AS total_revenue,
    ROUND(SUM(profit),2) AS total_profit,
    ROUND(SUM(profit)/SUM(sales)*100,2) AS profit_margin
FROM orders;

-- Category Performance
SELECT 
    category,
    ROUND(SUM(sales),2) AS revenue,
    ROUND(SUM(profit),2) AS profit,
    ROUND(SUM(profit)/SUM(sales)*100,2) AS margin
FROM orders
GROUP BY category;

-- Discount Impact
SELECT 
    discount,
    ROUND(SUM(sales),2) AS revenue,
    ROUND(SUM(profit),2) AS profit
FROM orders
GROUP BY discount
ORDER BY discount;

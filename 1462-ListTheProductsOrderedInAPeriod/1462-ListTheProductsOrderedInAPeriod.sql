-- Last updated: 9/10/2025, 12:56:54 AM
# Write your MySQL query statement below
SELECT product_name, SUM(unit) AS unit FROM Orders JOIN products as p ON p.product_id = orders.product_id WHERE order_date IN (SELECT order_date FROM Orders WHERE order_date LIKE '%2020-02%') GROUP BY orders.product_id HAVING unit >= 100;
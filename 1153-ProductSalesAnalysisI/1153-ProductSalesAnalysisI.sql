-- Last updated: 9/10/2025, 12:57:04 AM
# Write your MySQL query statement below
SELECT product_name, year, price FROM Sales as s JOIN Product as p ON s.product_id = p.product_id;
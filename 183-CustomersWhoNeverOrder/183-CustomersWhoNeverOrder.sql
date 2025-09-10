-- Last updated: 9/10/2025, 12:58:14 AM
# Write your MySQL query statement below
SELECT name as Customers FROM Customers WHERE id NOT IN (SELECT customerId FROM orders);
-- Last updated: 9/10/2025, 12:57:18 AM
# Write your MySQL query statement below
SELECT * FROM cinema WHERE (NOT description = 'boring') AND (id % 2 = 1) ORDER BY rating DESC;
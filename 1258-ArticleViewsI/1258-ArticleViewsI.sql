-- Last updated: 9/10/2025, 12:57:02 AM
# Write your MySQL query statement below
SELECT DISTINCT author_id as id FROM views WHERE author_id = viewer_id ORDER BY id ASC;
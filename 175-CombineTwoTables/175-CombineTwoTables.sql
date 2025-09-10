-- Last updated: 9/10/2025, 12:58:15 AM
# Write your MySQL query statement below
SELECT firstName, lastName, city, state FROM person as p LEFT JOIN address as a ON p.personID = a.personID;
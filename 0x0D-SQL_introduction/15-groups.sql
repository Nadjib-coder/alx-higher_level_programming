-- a script that lists the number of records with the same score in the table second_table
SELECT score, COUNT(*) AS number GROUP BY score ORDER BY nscore DESC;


-- Import in hbtn_0c_0 database this table dump
SELECT city, AVG(value) AS avg_temp FROM temperatures
GROUP BY cityORDER BY avg_temp DESC;


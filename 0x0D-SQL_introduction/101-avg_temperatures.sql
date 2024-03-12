-- Import in hbtn_0c_0 database this table dump: temperatures.sql
-- 
-- Write a script that displays the average temperature (Fahrenheit) by city ordered by temperature (descending).
USE hbtn_0c_0
CREATE TABLE IF NOT EXISTS temperature
(city VARCHAR(15), state VARCHAR (15), year INT, month INT, temp INT);
LOAD DATA
LOCAL INFILE 'temperature'
INTO TABLE temperature;
SELECT city, AVG(temp) as avg_temp
FROM temperature
GROUP BY city
ORDER BY avg_temp DESC;

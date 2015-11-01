# a column has some negative and some positive values, it is required to find the sum of negative numbers and the sum of the positive numbers in two separate columns.

SELECT 
	SUM(CASE WHEN num < 0 THEN num ELSE 0 END) as negSum
	SUM(CASE WHEN num > 0 THEN num ELSE 0 END) as posSum
FROM table_name;
# write a query to select only those rows which contains alphanumeric values.

SELECT * FROM table_name
WHERE LENGTH(TRIM(TRANSLATE(col1, '1234567890', ''))) > 0;
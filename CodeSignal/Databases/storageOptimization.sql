-- You noticed that your server is running out of free HDD space. You investigated and discovered that most of the space is taken up by the workers_info table, which has the following structure:

-- id: the unique worker ID;
-- name: the name of the worker;
-- date_of_birth: the worker's date of birth;
-- salary: the worker's salary.
-- One strange thing about this table is that a lot of its rows contain NULL values in some of the columns (except for the id column, which always contains a non-NULL value).

-- After thinking about this problem, you've decided to change the way you store data in workers_info. Instead of keeping the cells with NULL values in the table, you will only store id, column_name, and value columns. column_name will contain the name of a column that contains a non-NULL value for each id. value will be the value from this row, converted to a string. For dates, use the format YYYY-MM-DD.

-- Given the workers_info table, your task is to write a select statement which returns the following three columns: id, column_name, and value, that contain the workers' ids, the column names, and the stringified values, in the format described above. The output should be sorted in ascending order by id. Rows with the same id should be sorted by column names in the following order: name, date_of_birth, and then salary.

-- Example

-- For the following table workers_info, where empty cells stand for a NULL value

-- id	name	date_of_birth	salary
-- 1	Justin Penrose	1969-03-01	3000
-- 2			
-- 3	Robt Claire		
-- 10		1970-12-12	
-- 11			5000
-- 12	Yuk Kluge		4500
-- the output should be

-- id	column_name	value
-- 1	name	Justin Penrose
-- 1	date_of_birth	1969-03-01
-- 1	salary	3000
-- 3	name	Robt Claire
-- 10	date_of_birth	1970-12-12
-- 11	salary	5000
-- 12	name	Yuk Kluge
-- 12	salary	4500

CREATE PROCEDURE solution()
BEGIN
	/* Write your SQL here. Terminate each statement with a semicolon. */
	SELECT id, 'name' AS column_name, CAST(name AS CHAR) AS value FROM workers_info WHERE name IS NOT NULL
    UNION ALL
    SELECT id, 'date_of_birth' AS column_name, DATE_FORMAT(date_of_birth, '%Y-%m-%d') AS value FROM workers_info WHERE date_of_birth IS NOT NULL
    UNION ALL
    SELECT id, 'salary' AS column_name, CAST(salary AS CHAR) AS value FROM workers_info WHERE salary IS NOT NULL
    ORDER BY id, 
             CASE 
                 WHEN column_name = 'name' THEN 1
                 WHEN column_name = 'date_of_birth' THEN 2
                 WHEN column_name = 'salary' THEN 3
             END;
END
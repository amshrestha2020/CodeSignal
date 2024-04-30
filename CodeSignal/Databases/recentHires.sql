-- Your company has many different departments. Information about the employees working in these departments is stored in the pr_department, it_department, and sales_department tables, which have the following structures:

-- pr_department:
-- id: the unique (for this department) employee ID;
-- name: the name of the employee;
-- date_joined: the date this employee was hired by your company.
-- it_department:
-- id: the unique (for this department) employee ID;
-- name: the name of the employee;
-- date_joined: the date this employee was hired by your company.
-- sales_department:
-- id: the unique (for this department) employee ID;
-- name: the name of the employee;
-- date_joined: the date this employee was hired by your company.
-- Your task is to prepare a report that has the names of all the employees who were hired recently.

-- Given the pr_department, it_department, and sales_department tables, compose the result as follows: The resulting table should have one column names that contains the names of the last five people to join each department. The names of the employees from the pr_department should come first, followed by the it_department, and the sales_department will come last. The names of employees who work in the same department should be sorted in ascending order.

-- Example

-- The following tables pr_department

-- id	name	date_joined
-- 2	Bertha Neiman	2010-12-15
-- 3	Melissa Chace	2012-08-14
-- 4	Doyle Wiste	2015-01-02
-- 8	Libbie Troy	2016-03-04
-- 15	Noreen Bonner	2012-07-07
-- 42	Farah Dahlquist	2006-12-12
-- it_department

-- id	name	date_joined
-- 1	Farah Dahlquist	2017-01-15
-- 2	Mohammed Claycomb	2016-06-11
-- 3	Allen Reger	2015-08-12
-- 5	Jacque Fuhr	2013-04-01
-- 4	Joya Buss	2011-11-11
-- 6	Leonia Maultsby	2009-02-02
-- 7	Oliva Mcgarry	2008-05-05
-- and sales_department

-- id	name	date_joined
-- 3	Jayne Kravitz	2009-09-09
-- 4	Joya Buss	2008-08-08
-- 7	Edmond Kind	2007-07-07
-- the output should be

-- names
-- Bertha Neiman
-- Doyle Wiste
-- Libbie Troy
-- Melissa Chace
-- Noreen Bonner
-- Allen Reger
-- Farah Dahlquist
-- Jacque Fuhr
-- Joya Buss
-- Mohammed Claycomb
-- Edmond Kind
-- Jayne Kravitz
-- Joya Buss


CREATE PROCEDURE solution()
BEGIN
	/* Write your SQL here. Terminate each statement with a semicolon. */
	SELECT name as names
    FROM (
        (SELECT *, 1 AS dep FROM pr_department ORDER BY date_joined DESC, name LIMIT 5)
        UNION
        (SELECT *, 2 AS dep FROM it_department ORDER BY date_joined DESC, name LIMIT 5)
        UNION
        (SELECT *, 3 AS dep FROM sales_department ORDER BY date_joined DESC, name LIMIT 5)
        ) u
    ORDER BY dep, name;


END
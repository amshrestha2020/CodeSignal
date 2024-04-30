-- You work at a small startup company that only has a handful of employees. Since the company is so small, some of the employees have to work in several departments at once. Because of this, information about groups of employees that work in the same departments is stored in two separate tables, departments and employees. The tables are structured as follows:

-- departments:
-- dep_name: the unique department name;
-- employees:
-- emp_name: the employee's unique first name and surname.
-- Given the tables departments and employees, you have to prepare a report about company employees and the departments in which they work. To do this, you simply combine the rows of the two tables, then sort the resulting rows first by the departments' names and then by the employees' names.

-- Example

-- For the following tables departments

-- dep_name
-- IT
-- PD
-- and employees:

-- emp_name
-- Donald Cole
-- James Richard
-- John Tucker
-- the output should be

-- dep_name	emp_name
-- IT	Donald Cole
-- IT	James Richard
-- IT	John Tucker
-- PD	Donald Cole
-- PD	James Richard
-- PD	John Tucker


CREATE PROCEDURE solution()
BEGIN
	/* Write your SQL here. Terminate each statement with a semicolon. */
	SELECT
    d.dep_name,
    e.emp_name
FROM
    departments d
CROSS JOIN
    employees e
ORDER BY
    d.dep_name,
    e.emp_name;

END
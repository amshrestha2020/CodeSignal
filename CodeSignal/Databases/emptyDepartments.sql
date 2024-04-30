-- You've just started working for a large and successful company, and it's come as a shock to find that the records about the company's internal organization haven't been updated for ages. Some employees have changed their departments and some have resigned, and consequently, there are some departments that have no employees in them. You want to identify these departments.

-- Information about employees and departments is stored in two tables, employees and departments, which have the following structure:

-- employees:
-- id: the unique employee ID;
-- full_name: the employee's full name;
-- department: a foreign key referencing departments.id;
-- departments:
-- id: the unique department ID;
-- dep_name: the department name.
-- Given the tables employees and departments, write a select statement which returns only one column, dep_name, which contains all the departments in which there are no employees, sorted by id.

-- Example

-- For the following tables departments

-- id	dep_name
-- 1	IT
-- 2	HR
-- 3	Sales
-- 4	Warehousing
-- and employees

-- id	full_name	department
-- 1	James Miller	1
-- 2	Joseph Harvey	1
-- 3	Anna Lawson	2
-- 4	Arthur Saunders	3
-- the output should be

-- dep_name
-- Warehousing


CREATE PROCEDURE solution()
BEGIN
	/* Write your SQL here. Terminate each statement with a semicolon. */
	SELECT d.dep_name
    FROM departments d
    LEFT JOIN employees e ON d.id = e.department
    WHERE e.department IS NULL
    ORDER BY d.id;
END
-- The kingdom has been given terrible news: the King has passed away. While the nation is mourning, the noblemen need to decide who will take the throne next.

-- The late King had many children, and now it is necessary to determine their order of succession according to their seniority.

-- The list of the King's children is represented as a table Successors with the following attributes:

-- name: the child's name;
-- birthday: the date of their birthday (it is guaranteed that birthday dates are unique);
-- gender: their gender (a character equal to 'M' or 'F').
-- The resulting table should contain the names of the King's heirs in order of their succession to the throne as determined by their age, and preceded by their potential future titles (i.e. "King name" or "Queen name").

-- Example

-- For the following table Successors

-- name	birthday	gender
-- Amelia	1711-06-10	F
-- Anne	1709-11-02	F
-- Caroline	1713-06-10	F
-- Frederick	1707-02-01	M
-- Loisa	1724-12-18	F
-- Mary	1723-03-05	F
-- William	1721-04-26	M
-- The output should be

-- name
-- King Frederick
-- Queen Anne
-- Queen Amelia
-- Queen Caroline
-- King William
-- Queen Mary
-- Queen Loisa


CREATE PROCEDURE solution()
BEGIN
	/* Write your SQL here. Terminate each statement with a semicolon. */
	SELECT 
  CONCAT(
    CASE WHEN gender = 'M' THEN 'King ' ELSE 'Queen ' END,
    name
  ) AS name
FROM 
  Successors
ORDER BY 
  birthday;

END
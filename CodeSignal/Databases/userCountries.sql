-- You are really interested in statistics, and your new project is to gather some information about the users of a big social network. More specifically, you want to know which countries these users are from. Using the social network's API, you managed to collect enough data to compose two tables users and cities, which have the following structures:

-- users:
-- id: the unique user ID;
-- city: the name of the city where this user lives;
-- cities:
-- city: a unique city name;
-- country: the name of the country where this city is located.
-- Given the tables users and cities, write a select statement that returns two columns id and country consisting of user ids and the countries where they live respectively. If a user's city is missing from the cities table, the country column should contain "unknown" instead.

-- Return the table sorted by users' ids.

-- Example

-- For the following table users

-- id	city
-- 1	San Francisco
-- 2	Moscow
-- 3	London
-- 4	Washington
-- 5	New York
-- 6	Saint Petersburg
-- 7	Helsinki
-- and the following table cities

-- city	country
-- Moscow	Russia
-- Saint Petersburg	Russia
-- San Francisco	USA
-- Washington	USA
-- New York	USA
-- London	England
-- the output should be

-- id	country
-- 1	USA
-- 2	Russia
-- 3	England
-- 4	USA
-- 5	USA
-- 6	Russia
-- 7	unknown


CREATE PROCEDURE solution()
BEGIN
	/* Write your SQL here. Terminate each statement with a semicolon. */
	SELECT u.id, COALESCE(c.country, 'unknown') AS country
FROM users u
LEFT JOIN cities c ON u.city = c.city
ORDER BY u.id;

END
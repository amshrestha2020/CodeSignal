-- You are curious about the geographical distribution of CodeSignal users, so you have created a list of countries along with the number of registered users from each. Your task now is to calculate the number of users on each continent.

-- The information about the countries is stored in a table countries, which has 3 columns:

-- country: the name of the country;
-- continent: the name of the continent where the country is located;
-- users: the number of users registered on CodeSignal in the country.
-- The answer should be a table with 2 columns, continent and users, sorted by the number of users in decreasing order.

-- Example

-- For the following table countries

-- country	continent	users
-- Armenia	Europe	1000
-- France	Europe	1300
-- Russia	Europe	3000
-- USA	North America	5000
-- the resulting table should be

-- continent	users
-- Europe	5300
-- North America	5000


CREATE PROCEDURE solution()
BEGIN
	/* Write your SQL here. Terminate each statement with a semicolon. */
	SELECT
    continent,
    SUM(users) AS users
FROM countries
GROUP BY continent
ORDER BY users DESC;

END
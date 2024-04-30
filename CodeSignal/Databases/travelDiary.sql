-- You are an avid traveler and you've visited so many countries that when people ask you where you've been, you can't even remember all of them! Luckily, every time you travel somewhere you write down the trip information in your diary. Now you want to get a list of all the different countries that you have visited using the information in your diary.

-- The diary is represented as a table diary, which has the following columns:

-- id: the unique ID of the trip;
-- travel_date: the date the trip began;
-- country: the country to which you traveled.
-- Given this diary table, create a semicolon-separated list of all the distinct countries you've visited, sorted lexicographically, and put the list in a table that has a single countries column.

-- Example

-- For the following table diary

-- id	travel_date	country
-- 1	2008-05-12	Ireland
-- 2	2010-11-04	France
-- 3	2005-10-02	Australia
-- 4	2008-06-08	Japan
-- 5	2010-08-27	Austria
-- 6	2009-02-15	France
-- the output should be

-- countries
-- Australia;Austria;France;Ireland;Japan

CREATE PROCEDURE solution()
BEGIN
	/* Write your SQL here. Terminate each statement with a semicolon. */
	SELECT GROUP_CONCAT(DISTINCT country ORDER BY country) AS countries
FROM diary;

END
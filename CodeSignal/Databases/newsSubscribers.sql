-- You are managing a small newspaper subscription service. Anyone who uses it can subscribe to a large number of different newspapers for a full year or just a half year.

-- The information about subscriptions is stored in the full_year and half_year tables, which have the following structures:

-- full_year:
-- id: the unique subscription ID;
-- newspaper: the newspaper's name;
-- subscriber: the name of the subscriber.
-- half_year
-- id: the unique subscription ID;
-- newspaper: the newspaper's name;
-- subscriber: the name of the subscriber.
-- Given the full_year and half_year tables, compose the result as follows: The resulting table should have one column subscriber that contains all the distinct names of anyone who is subscribed to a newspaper with the word Daily in its name. The table should be sorted in ascending order by the subscribers' first names.

CREATE PROCEDURE solution()
BEGIN
	/* Write your SQL here. Terminate each statement with a semicolon. */
	SELECT DISTINCT subscriber
FROM (
    SELECT subscriber FROM full_year WHERE newspaper LIKE '%Daily%'
    UNION
    SELECT subscriber FROM half_year WHERE newspaper LIKE '%Daily%'
) AS subscriptions
ORDER BY subscriber;

END
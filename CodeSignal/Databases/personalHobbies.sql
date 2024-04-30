-- You've been looking for new friends on the Internet. You just came across a cool website that helps people all over the world become friends by suggesting perfect friend candidates based on the information in users' profiles.

-- The system suggested some people for you to reach out to, and you're ready to make a move. However, you don't want to exercise your communication skills in vain, which is why prior to contacting a person you want to make sure you'll have something in common to talk about. The best option is to check whether they have the same hobbies you do, which are sports and reading.

-- You downloaded the list of suggested people and saved it in the people_hobbies table, which has the following structure:

-- name - the unique person's name;
-- hobbies - a list of hobbies the person has (this column is of the datatype set).
-- Given the people_hobbies table, your goal is to return the sorted names of people who have sports and reading in their list of hobbies.

-- Example

-- For the given table people_hobbies

-- name	hobbies
-- Adam	swimming
-- Amy	reading,sports,swimming
-- Carl	filmwatching,writing
-- Carol	reading,swimming
-- Deril	sports
-- Jake	reading,swimming
-- Lola	reading,sports,painting
-- Nina	sports,painting
-- Sam	sports
-- the output should be

-- name
-- Amy
-- Lola
-- As you can see, only Amy and Lola have both reading and sports in their hobbies lists.

CREATE PROCEDURE solution()
BEGIN
	/* Write your SQL here. Terminate each statement with a semicolon. */
	SELECT name
FROM people_hobbies
WHERE FIND_IN_SET('sports', hobbies) > 0 AND FIND_IN_SET('reading', hobbies) > 0
ORDER BY name;

END

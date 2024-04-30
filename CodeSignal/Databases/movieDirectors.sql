-- You want to expand your movie collection, but you don't really have any preferences so you're not sure where to start. After some consideration, you decide that you should start by finding more movies from award-winning directors whose movies you already own and who have shot a movie somewhat recently.

-- To find the directors whose movies you might want to consider watching in the first place, you've created a database of all the films you already own and stored them in a moviesInfo table, which has the following structure:

-- title: the title of the movie;
-- director: the director of this movie;
-- year: the year the movie was released;
-- oscars: the number of the Academy Awards this movie received.
-- Given the moviesInfo table, compose the list of directors you should consider watching more movies from. The resulting table should have a single director column and contain the names of film directors such that:

-- they shot movies after the year 2000;
-- the total number of Oscar awards these movies received is more than 2.
-- The table should be sorted by the directors' names in ascending order.

-- Example

-- For the following table moviesInfo

-- title	director	year	oscars
-- BoBoiBoy: The Movie	Nizam Razak	2016	0
-- Inception	Christopher Nolan	2010	4
-- Interstellar	Christopher Nolan	2014	1
-- Munna Bhai M.B.B.S.	Rajkumar Hirani	2003	0
-- My Dear Brother	Ertem Egilmez	1973	0
-- Rocky John	G. Avildsen	1976	3
-- The Nights of Cabiria	Federico Fellini	1957	1
-- The Sixth Sense	M. Night Shyamalan	1999	6
-- The Sixth Sense	M. Night Shyamalan	1999	6
-- Tokyo Story	Yasujirô Ozu	1953	0
-- Yojimbo	Akira Kurosawa	1961	1
-- the output should be

-- director
-- Christopher Nolan


CREATE PROCEDURE solution()
BEGIN
	/* Write your SQL here. Terminate each statement with a semicolon. */
	SELECT DISTINCT director
FROM moviesInfo
WHERE year > 2000
GROUP BY director
HAVING SUM(oscars) > 2
ORDER BY director;

END
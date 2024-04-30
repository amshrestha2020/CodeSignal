-- You're going on vacation in a big city, and you've prepared a list of all the sights you'd like to visit. As you don't have much time and can't spend a whole day at one interesting place, you want to visit several sights per day and walk from one site to another. But walking a long distance might be boring, so you won't walk between two places if the distance between them is 5 km or more.

-- To find the route that you should take, you are going to find all pairs of places that are less than 5 km from each other.

-- The places of interests are stored in a table sights, which has the following attributes:

-- id: the unique ID of the place;
-- name: the name of the place;
-- x: the x coordinate of the place;
-- y: the y coordinate of the place.
-- The distance between the places is calculated with the assumption that they are just points on a 2D map.

-- Given the sights table, find all pairs of places that are less than 5 km from each other and return them as a table with the columns place1 and place2. Sort them in lexicographical order. The places in the pairs should also be sorted lexicographically.

-- Example

-- For the following table sights

-- id	name	x	y
-- 1	Tower of London	51508.026	-7.5939
-- 2	Trafalgar Square	51508.040	-12.7899
-- 3	London Eye	51503.538	-11.9371
-- 4	The Shard	51504.533	-8.6028
-- the output should be

-- place1	place2
-- London Eye	The Shard
-- London Eye	Trafalgar Square
-- The Shard	Tower of London

CREATE PROCEDURE solution()
BEGIN
	/* Write your SQL here. Terminate each statement with a semicolon. */
	SELECT DISTINCT
    LEAST(s1.name, s2.name) AS place1,
    GREATEST(s1.name, s2.name) AS place2
FROM sights s1
JOIN sights s2 ON s1.id < s2.id
WHERE SQRT(POW(s1.x - s2.x, 2) + POW(s1.y - s2.y, 2)) < 5
ORDER BY place1, place2;

END

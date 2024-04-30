-- The store you're working for has decided to organize a special holiday event: every 4th purchase made during this event grants the lucky person who made it a special prize.

-- All purchases made during the event are stored in the database table purchases with the following structure:

-- timestamp: unique purchase timestamp;
-- buyer_name: the name of the person who made this purchase.
-- Given the purchases table, compose the resulting table with one column winners containing the names of the buyers who won the special prize by making a purchase number k * 4 for some integer k. The numbering of the purchases starts with 1.
-- Note, that each person can get no more than one prize (i.e. their name can occur in the answer at most once).
-- The table should be sorted by the winners' names in ascending order.

-- Example

-- For the following table purchases

-- timestamp	buyer_name
-- 2014-11-09 15:23:05	Frank West
-- 2014-11-09 20:11:02	Terrence Alexander
-- 2014-11-10 12:10:00	Sandy Cohen
-- 2014-11-10 13:00:11	Frank West
-- 2014-11-10 14:09:10	Sandy Cohen
-- 2014-11-10 14:15:15	Leonard Grant
-- 2014-11-10 17:09:10	Frank West
-- 2014-11-10 19:09:10	Diane Tucker
-- 2014-11-11 18:09:11	Pauline Ross
-- 2014-11-11 20:00:00	Jasmine Gibson
-- 2014-11-12 10:12:00	Kim Neal
-- 2014-11-12 10:12:01	Frank West
-- 2014-11-12 15:14:42	Sean Kim
-- the output should be

-- winners
-- Diane Tucker
-- Frank West
-- because Frank West made the 4th and the 12th purchases, and Diane Tucker's purchase was the 8th.



CREATE PROCEDURE solution()
BEGIN
	/* Write your SQL here. Terminate each statement with a semicolon. */
	SET @purchase = 0;
	SELECT DISTINCT buyer_name AS winners
    FROM(
        SELECT * FROM purchases
        WHERE (@purchase:=@purchase + 1)%4 = 0
        ORDER BY timestamp) t
    ORDER BY buyer_name;
END
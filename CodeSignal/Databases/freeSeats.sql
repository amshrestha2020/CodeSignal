-- You're working on the tech support team of an airline company, and your boss has asked you to implement a feature that shows the number of available seats on every flight.

-- Information about the airline is stored in three tables - flights, planes, and purchases, respectively. The tables are structured as follows:

-- flights:
-- flight_id: the unique flight id;
-- plane_id: the id of the plane making the flight.
-- planes:
-- plane_id: the unique plane id;
-- number_of_seats: the number of seats on the plane.
-- purchases:
-- flight_id: the flight id of the purchase;
-- seat_no: the seat number of the purchase.
-- It is guaranteed that in the purchases table, the pairs (flight_id, seat_no) are unique.

-- With the information provided in the database, you need to calculate the number of seats that are not yet purchased for each flight_id.

-- Given tables flights, planes, and purchases, write a stored procedure that returns a rowset as follows: The resulting rowset should have columns flight_id and free_seats, where for each flight_id, free_seats is the number of seats that have not been purchased yet. The rows of the rowset should be ordered by flight_id in ascending order. It is guaranteed that the information in table purchases is consistent and there are no purchases for non-existing flight_ids or seat_nos.

-- Example

-- For the following tables flights

-- flight_id	plane_id
-- 111	128
-- 87	157
-- 100	23
-- 121	23
-- planes

-- plane_id	number_of_seats
-- 128	5
-- 23	7
-- 157	4
-- 239	2
-- and purchases

-- flight_id	seat_no
-- 111	1
-- 87	1
-- 87	7
-- 100	5
-- the output should be

-- flight_id	free_seats
-- 87	2
-- 100	6
-- 111	4
-- 121	7
-- Flight number 87 has 4 seats, and 2 of them have been purchased;
-- Flight number 100 has 7 seats, and one of them has been purchased;
-- Flight number 111 has 5 seats, and one of them has been purchased;
-- Flight number 121 has 7 seats, and none of them have been purchased.
-- MySQL hint

-- To return a row set in a MySQL stored procedure, the last statement in the stored procedure should be a SELECT statement, followed by a semi-colon.
-- E.g.

-- CREATE PROCEDURE solution()
-- BEGIN
--         SELECT * FROM planes;
-- END


CREATE PROCEDURE solution()
BEGIN
	/* Write your SQL here. Terminate each statement with a semicolon. */
	SELECT f.flight_id, p.number_of_seats - COUNT(pr.seat_no) AS free_seats
    FROM flights f
    JOIN planes p ON f.plane_id = p.plane_id
    LEFT JOIN purchases pr ON f.flight_id = pr.flight_id
    GROUP BY f.flight_id
    ORDER BY f.flight_id;
END
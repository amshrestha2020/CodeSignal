-- You are developing a calendar application that will allow users to schedule various events on different dates. The dates are all stored in the server local time as a DATETIME. You want to display the dates using the settings specified by the user.

-- Event dates and user settings are stored in the events and settings tables, which have the following structures:

-- events:
-- event_id: the unique event ID;
-- date: the time and date of the event;
-- user_id: the ID of the user who scheduled this event.
-- settings
-- user_id: the unique ID of the user with these settings;
-- timeshift: the number of minutes the user's time differs from the server (this could potentially be negative or zero);
-- hours: the number of hours in the user's clock (either 12 or 24).
-- The displayed dates should have the format yyyy-mm-dd hh:mm if the user's clock has 24 hours. Otherwise, the format should be yyyy-mm-dd hh:mm <p>, where <p> is either AM or PM depending on the time.

-- Given the events and settings tables, compose the result as follows: The resulting table should have two columns, event_id and formatted_date, that contain the event IDs and the formatted event dates according to settings of the user who scheduled that event, respectively. The table should be sorted in ascending order by the event IDs.

-- Example

-- The following tables events

-- event_id	date	user_id
-- 1	2011-11-11 13:37:00	4242
-- 2	2012-12-12 04:04:00	4987
-- 3	2016-01-01 11:19:00	4242
-- 4	2011-11-11 13:37:00	4987
-- and settings

-- user_id	timeshift	hours
-- 1	30	24
-- 4242	0	24
-- 4987	60	12
-- the output should be

-- event_id	formatted_date
-- 1	2011-11-11 13:37
-- 2	2012-12-12 05:04 AM
-- 3	2016-01-01 11:19
-- 4	2011-11-11 02:37 PM


CREATE PROCEDURE solution()
BEGIN
	/* Write your SQL here. Terminate each statement with a semicolon. */
	SELECT event_id, DATE_FORMAT(ADDDATE(date, INTERVAL timeshift MINUTE), CONCAT('%Y-%m-%d ',IF(hours=12,'%h:%i %p','%H:%i'))) AS formatted_date
    FROM events JOIN settings USING(user_id)
    ORDER BY event_id;

END
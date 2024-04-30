-- You're very busy and have a lot of important events coming up. In order to ensure that you don't forget any of these events, you have decided to organize them.

-- The information about your events is stored in the table events, which has the structure:

-- id: unique event id;
-- name: the event name;
-- event_date: the event date in the format YYYY-MM-DD;
-- participants: the number of people that are going to attend this event.
-- After some thinking, you decide that it would be easier to navigate though your schedule if you could see all the events ordered by the weekday on which they are scheduled. In order to do so, you want to sort all the events by the weekdays of their event_dates, meaning that Monday events should come first, Tuesday events should come next, and so on, with Sunday events coming last. In the case of a tie, the participants should be a tie-breaker; an event with the largest number of participants should go first, because events with more attendees are more important. It is guaranteed that there are no events that have the same event_date and the same number of participants.

-- Given the table events, sort it as described above and return the resulting table.

-- Example

-- For the following table events

-- id	name	event_date	participants
-- 1	Dinner	2016-11-27	3
-- 2	Comic-con	2016-10-25	100
-- 3	Christmas	2016-12-31	5000
-- 4	Meeting	2016-10-18	300
-- the output should be

-- id	name	event_date	participants
-- 4	Meeting	2016-10-18	300
-- 2	Comic-con	2016-10-25	100
-- 3	Christmas	2016-12-31	5000
-- 1	Dinner	2016-11-27	3
-- Meeting and Comic-con are both scheduled for Tuesdays, but Meeting is more important because its participants number is bigger. Christmas is scheduled for Saturday and Dinner is scheduled for Sunday.



CREATE PROCEDURE solution()
BEGIN
	/* Write your SQL here. Terminate each statement with a semicolon. */
	SELECT id, name, event_date, participants
FROM events
ORDER BY 
  CASE 
    WHEN DAYOFWEEK(event_date) = 1 THEN 8
    ELSE DAYOFWEEK(event_date)
  END,
  participants DESC;

END
-- You are developing an alarm clock app that works as follows: the user can set a date and a time, and the app will ring every week at the given time, starting at the given date until the end of this given's date year.

-- The starting date is the only record in the userInput table, which has the following structure:

-- input_date: the date and time of the first alarm (of a DATETIME type).
-- Given the table, your task is to write a select statement which returns a single column alarm_date. This column should contain all dates (including the time) when the alarm clock will ring. The entries should be arranged in ascending chronological order.

-- Example

-- For the following table userInput

-- input_date
-- 2016-10-23 22:00:00
-- the output should be

-- alarm_date
-- 2016-10-23 22:00:00
-- 2016-10-30 22:00:00
-- 2016-11-06 22:00:00
-- 2016-11-13 22:00:00
-- 2016-11-20 22:00:00
-- 2016-11-27 22:00:00
-- 2016-12-04 22:00:00
-- 2016-12-11 22:00:00
-- 2016-12-18 22:00:00
-- 2016-12-25 22:00:00
-- example

CREATE PROCEDURE solution()
BEGIN
	/* Write your SQL here. Terminate each statement with a semicolon. */
	DROP TABLE IF EXISTS tmp;
  CREATE TABLE IF NOT EXISTS tmp (alarm_date DATETIME);
  SELECT input_date FROM userInput INTO @ldate;
  SET @y = YEAR(@ldate) + 1;
  test_loop : LOOP
    IF (YEAR(@ldate) = @y) THEN
      LEAVE test_loop;
    END IF;

    INSERT INTO tmp VALUES(@ldate);
    SET @ldate = ADDDATE(@ldate, INTERVAL 1 WEEK);
  END LOOP; 
  SELECT alarm_date FROM tmp;

END
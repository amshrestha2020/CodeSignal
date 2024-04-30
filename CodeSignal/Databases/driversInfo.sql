-- Your company is an authorized Chevrolet dealer, and you have your own database of the clients who've come to you for vehicle inspections. Right now it's not very convenient to analyze because it contains only the information retrieved during each inspection. You'd like to make this database easier to use.

-- Information about the inspections is given in the table inspections, which has the following columns:

-- inspection_id: the unique inspection ID;
-- driver_name: the name of the driver;
-- date: the inspection date (guaranteed to be distinct for each driver);
-- miles_logged: the number of miles the vehicle has covered since the previous inspection (or since the time of purchase if it's the car's first inspection).
-- Your goal is to make a new table with a single summary column that contains the following information:

-- The first row should contain the total number of miles covered by all the drivers combined;
-- The following rows should contain information about each driver, sorted by the drivers' names:
-- The first row should contain the driver's name, the total number of inspections, and the total number of miles covered;
-- The following rows should, for each inspection, contain the date of the inspection and the miles covered since the previous inspection (or the purchase time). The entries should be sorted by the inspection dates.
-- This information should be given in the following format:

-- summary
--  Total miles driven by all drivers combined: <the sum of all driven miles>
--  Name: [...]; number of inspections: [...]; miles driven: [...]
--   date: [...]; miles covered: [...]
--   date: [...]; miles covered: [...]
--   ...
--  Name: [...]; number of inspections: [...]; miles driven: [...]
--   ...
-- Note: Every row should start with a whitespace character, and the rows containing information about the inspections should should start with two whitespace characters.

-- Example

-- For the following table inspections

-- inspection_id	driver_name	date	miles_logged
-- 1	Gary	2014-03-15	256
-- 2	Dave	2014-01-18	231
-- 3	Dave	2014-01-16	45
-- 4	Gary	2014-02-03	30
-- 5	Dave	2014-01-17	180
-- the output should be

-- summary
--  Total miles driven by all drivers combined: 742
--  Name: Dave; number of inspections: 3; miles driven: 456
--   date: 2014-01-16; miles covered: 45
--   date: 2014-01-17; miles covered: 180
--   date: 2014-01-18; miles covered: 231
--  Name: Gary; number of inspections: 2; miles driven: 286
--   date: 2014-02-03; miles covered: 30
--   date: 2014-03-15; miles covered: 256


CREATE PROCEDURE solution()
BEGIN
	/* Write your SQL here. Terminate each statement with a semicolon. */
	DECLARE done INT DEFAULT FALSE;
    DECLARE name VARCHAR(250) DEFAULT '';
    DECLARE cur1 CURSOR FOR SELECT * FROM names;
    DECLARE CONTINUE HANDLER FOR NOT FOUND SET done = TRUE;
    DROP TABLE IF EXISTS tmp;
    CREATE TEMPORARY TABLE tmp (summary VARCHAR(250));
    DROP TABLE IF EXISTS names;
    CREATE TEMPORARY TABLE names AS SELECT DISTINCT driver_name FROM inspections
    ORDER BY driver_name;
    SET @name = '';
    OPEN cur1;
    
    INSERT INTO tmp VALUES(CONCAT(' Total miles driven by all drivers combined: ', (SELECT SUM(miles_logged) FROM inspections)));
    
read_loop: LOOP
    FETCH cur1 INTO name;
    IF done THEN
      LEAVE read_loop;
    END IF;
    INSERT INTO tmp VALUES((SELECT CONCAT(' Name: ', driver_name, '; number of inspections: ', COUNT(*), '; miles driven: ', SUM(miles_logged)) AS summary FROM inspections GROUP BY driver_name HAVING driver_name = name));
    INSERT INTO tmp (summary)
        SELECT CONCAT('  date: ', date, '; miles covered: ', miles_logged) AS summary FROM inspections WHERE driver_name = name
    ORDER BY date;
  END LOOP;

  CLOSE cur1;
  SELECT summary FROM tmp;
END
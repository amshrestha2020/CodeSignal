-- Your company's accounting department hasn't been doing great work lately, and they've been very sloppy when entering information into their database.

-- The information about each accounting document is stored in a documents table with 2 columns:

-- id: the unique id of the document;
-- date: the date the document was created, as a string in the format YYYY-MM-DD (of type VARCHAR(10)). Since input has been sloppy, the leading zeros of days and months have sometimes been omitted.
-- The omission of these leading zeros for days and months in the date column is making operations on the database prone to errors. To minimize the number of errors without changing the table structure, you need to translate all the dates to ISO format YYYY-MM-DD.

-- Given the documents table, return a table with one column date_iso that contains all the dates from documents sorted by the ids of the corresponding documents.

-- Example

-- For the following table documents

-- id	date_str
-- 1	2000-1-1
-- 2	2014-8-21
-- 3	2002-03-07
-- 4	2008-10-5
-- 5	2016-12-17
-- the output should be

-- date_iso
-- 2000-01-01
-- 2014-08-21
-- 2002-03-07
-- 2008-10-05
-- 2016-12-17


CREATE PROCEDURE solution()
BEGIN
	/* Write your SQL here. Terminate each statement with a semicolon. */
	SELECT Date(date_str) AS date_iso
    FROM documents
    ORDER BY id;

END
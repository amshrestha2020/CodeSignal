-- You recently started a new job, and you were frustrated to discover that the company you joined has a very poorly written front-end client application. It doesn't even have validation checks for data entered by users! The biggest problem is with the phone_number field, which your company uses to send automatic notifications to users.

-- Your first task as a company employee is to retrieve all the valid records from the given table of phone numbers. The record is valid if its phone_number is a valid American or Canadian phone number, which means that it has a format of 1-###-###-#### or (1)###-###-####, where # stands for any digit from 0 to 9.

-- Information is stored in the table phone_numbers, which has the following fields:

-- name: the user's first name;
-- surname: the user's unique surname;
-- phone_number: the user's unique phone number.
-- You should return a new table that contains only the valid records from the phone_numbers table, sorted by the users' surnames.

-- Example

-- For the following table phone_numbers

-- name	surname	phone_number
-- Cornelius	Walsh	1-234-567-8910
-- Frank	McKenzie	1-2345-678-911
-- John	Smith	(1)111-111-1111
-- Lester	Goodwin	(1)-111-111-1111
-- the output should be

-- name	surname	phone_number
-- John	Smith	(1)111-111-1111
-- Cornelius	Walsh


CREATE PROCEDURE solution()
BEGIN
	/* Write your SQL here. Terminate each statement with a semicolon. */
	SELECT *
    FROM phone_numbers
    WHERE phone_number REGEXP '^1-[0-9]{3}-[0-9]{3}-[0-9]{4}$' OR phone_number REGEXP '^\\(1\\)[0-9]{3}-[0-9]{3}-[0-9]{4}$'
    ORDER BY surname;
	
END
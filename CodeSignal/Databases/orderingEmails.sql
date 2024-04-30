-- You've started to receive a lot of emails every day, and you decide to sort them in order to make it quicker to navigate through them.

-- Information about your emails is stored in a table emails, which has the following structure:

-- id: the unique email id;
-- email_title: the title of the email;
-- size: the size of the email's body in bytes.
-- You decide to sort all the emails by their body sizes in descending order, because you think that the bigger an email is the more important it is. However, you don't like having the sizes written in bytes because they are usually too large and don't make much sense. You want them to be written in kilobytes (1 Kb = 210 bytes) and megabytes (1 Mb = 220 bytes) instead, rounded down if necessary. For example, 21432432 bytes is equal to 20 megabytes and 460912 bytes, so the result should be rounded down to 20 Mb.

-- Given the table emails, build a table as follows: The resulting table should have the columns id, email_title, and short_size, and should be sorted in descending order by the initial sizes of the emails. It is guaranteed that all the emails are of unique sizes, so there will not be any ties.

-- Example

-- For the following table emails

-- id	email_title	size
-- 1	You won 1M dollars!	21432432
-- 2	You are fired	312342
-- 3	Black Friday is coming	323
-- 4	Spam email	23532
-- 5	Your requested backup	234234324
-- the output should be

-- id	email_title	short_size
-- 5	Your requested backup	223 Mb
-- 1	You won 1M dollars!	20 Mb
-- 2	You are fired	305 Kb
-- 4	Spam email	22 Kb
-- 3	Black Friday is coming


CREATE PROCEDURE solution()
BEGIN
	/* Write your SQL here. Terminate each statement with a semicolon. */
	SELECT id, email_title, 
        CASE
        WHEN size >= 1048576 THEN CONCAT(FLOOR(size / 1048576), ' Mb')
        ELSE CONCAT(FLOOR(size / 1024), ' Kb')
        END  as short_size
        FROM emails
        ORDER BY size DESC;

END
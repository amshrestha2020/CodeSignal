-- In the past, straight "A" students have gotten scholarships to reward them for their excellent grades. This year, though, there has been an increase in the number of detentions given to excellent students, so the administration is going to change the rules. In order to encourage the levels of misbehavior to go down, only well-behaved students will be awarded with scholarships this year.

-- Information about the straight "A" students is stored in the table candidates, and information about all the detentions is stored in the table detentions. Here are their structures:

-- candidates
-- candidate_id: the unique candidate ID;
-- candidate_name: the name of the candidate;
-- detentions
-- detention_date: the date of the detention (of the date type);
-- student_id: the id of the student who got the detention.
-- Your task is to figure out which students should get the scholarships this year. Given the candidates and detentions tables, return a table with a single student_id column containing the IDs of the students who should get scholarships - students from the candidates table who've never gotten a detention. The IDs of the students in the resulting table should be sorted in ascending order.

-- Example

-- For the following tables candidates

-- candidate_id	candidate_name
-- 12	Gerlinde Addens
-- 35	Gerbern Abbey
-- 44	Edmond Ramsay
-- 58	Svanhild Lacey
-- 103	Nita Simons
-- and detentions

-- detention_date	student_id
-- 2015-10-21	12
-- 2015-11-19	91
-- 2016-02-11	87
-- 2015-12-26	44
-- 2016-01-19	91
-- 2015-09-10	91
-- 2015-12-30	12
-- 2016-05-19	58
-- the output should be

-- student_id
-- 35
-- 103
-- Only Gerbern Abbey and Nita Simons never got detention, so they will get the scholarships this year.

-- The dates in the example are given in the YYYY-MM-DD format.



CREATE PROCEDURE solution()
BEGIN
	/* Write your SQL here. Terminate each statement with a semicolon. */
	SELECT DISTINCT c.candidate_id AS student_id
FROM candidates c
LEFT JOIN detentions d ON c.candidate_id = d.student_id
WHERE d.student_id IS NULL
ORDER BY c.candidate_id;


END
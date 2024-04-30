-- You are collecting some statistics about strings in the table strs, which only has one column:

-- str - a unique string that consists only of lowercase English letters.
-- Your goal is to return a new table ans, which has the following columns:
-- letter - a unique lowercase English letter;
-- total - the total number of occurrences of this letter in all the strings from table strs;
-- occurrence - the number of strings from table strs in which this letter occurs at least once;
-- max_occurrence - the maximal number of occurrences of this letter in a single string;
-- max_occurence_reached - the number of strings in which this maxumal number of occurrences is reached.
-- The rows should be ordered lexicographically by letter. For letters that are not contained in the strs table, don't add a row to the output table (i.e., all integers in the total column should be positive).

-- Example

-- For given table strs

-- str
-- aa
-- aaaa
-- aab
-- abaaba
-- bbbbb
-- the output should be

-- letter	total	occurrence	max_occurrence	max_occurrence_reached
-- a	12	4	4	2
-- b	8	3	5


CREATE PROCEDURE solution()
BEGIN
	/* Write your SQL here. Terminate each statement with a semicolon. */
	DECLARE c INT DEFAULT 97;
DROP TABLE IF EXISTS alpha;
CREATE TEMPORARY TABLE alpha (letter VARCHAR(2));

WHILE c <= 122 DO
    INSERT INTO alpha VALUES(CHAR(c));
    SET c = c + 1;
END WHILE;

SELECT 
    letter,
    CHAR_LENGTH(tstring) - CHAR_LENGTH(REPLACE(tstring, letter, '')) AS total,
    (SELECT COUNT(*) FROM strs WHERE INSTR(str, letter) > 0) AS occurrence,
    (SELECT MAX(cnt) FROM (SELECT CHAR_LENGTH(str) - CHAR_LENGTH(REPLACE(str, letter, '')) AS cnt FROM strs) AS sub) AS max_occurrence,
    (SELECT COUNT(*) FROM strs WHERE CHAR_LENGTH(str) - CHAR_LENGTH(REPLACE(str, letter, '')) = (SELECT MAX(cnt) FROM (SELECT CHAR_LENGTH(str) - CHAR_LENGTH(REPLACE(str, letter, '')) AS cnt FROM strs) AS sub)) AS max_occurrence_reached
FROM 
    alpha, (SELECT GROUP_CONCAT(str SEPARATOR '') AS tstring FROM strs) t
HAVING 
    total > 0;


END
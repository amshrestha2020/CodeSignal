-- You returned from vacation with a huge suitcase full of presents. Unfortunately, you forgot the correct combination for the combination lock on the bag, and now you have to try all of them until you find the correct one. You're curious about how many possible combinations the lock has.

-- The combination lock consists of several rotating discs, where each disc has its own set of possible characters. You have a table discs which stores the information about these discs and has the following structure:

-- id: the unique ID of a disc;
-- characters: the list of characters the disc has (the characters are guaranteed to be unique);
-- color: the color of the disc.
-- Calculate the total number of all possible combinations that the lock has, and return it as a table that has only one column combinations and one row.

-- Example

-- For the following table discs

-- id	characters	color
-- 1	code	blue
-- 2	fights	white
-- the output should be

-- combinations
-- 24
-- The set of possible characters for the first disc is equal to 4, and the set for the second disc is 6, so the total number of combinations is 4 * 6 = 24.

CREATE PROCEDURE solution()
BEGIN
	/* Write your SQL here. Terminate each statement with a semicolon. */
	SELECT ROUND(EXP(SUM(LOG(CHAR_LENGTH(characters))))) AS combinations
    FROM discs;
END
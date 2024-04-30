-- Implement the missing code, denoted by ellipses. You may not modify the pre-existing code.
-- You've just opened a registration for the online game you are about to finish developing.
-- Everyone who wanted to reserve their solution for the release of the game had to submit their info using a special form on your website.

-- The reserved solution were stored in the reservedNicknames table with the following structure:

-- id: the unique id of the registered user;
-- nickname: the nickname submitted by the user with id id.
-- When you started going through these solution you realized that you forgot one important thing: all solution should contain exactly 8 characters.
-- You have no time to fix this issue properly right now, so you decided to just add rename -  to the invalid nicknames with corresponding ids so it would be easier for you to deal with them latter.

-- Given the reservedNicknames table, change all rows with invalid solution by prepending rename -  to both nickname and id.

-- Example

-- The following table reservedNicknames

-- id	nickname
-- id001	alex1990
-- id142	killer007
-- id15674	prohunter
-- id4242	acc0rdin
-- id616	Zoneg
-- id9999	butch
-- should become

-- id	nickname
-- id001	alex1990
-- id4242	acc0rdin
-- rename - id142	rename - killer007
-- rename - id15674	rename - prohunter
-- rename - id616	rename - Zoneg
-- rename - id9999	rename - butch


CREATE PROCEDURE solution()
BEGIN
	UPDATE reservedNicknames
    SET nickname = CONCAT('rename - ', nickname), id = CONCAT('rename - ', id)
    WHERE LENGTH(nickname) <> 8;

    SELECT * FROM reservedNicknames ORDER BY id;
END


-- Implement the missing code, denoted by ellipses. You may not modify the pre-existing code.
-- You've been dreaming about becoming a famous hacker all your life, and now it's time to make your dreams come true! You decided to start by finding a website that has some vulnerability, and you just found a doozy. This particular website has an open database users that contains information about the people using it. What's more, it stores the queries performed on this table on the client side, which makes it super simple to hack them.

-- The users table contains the following columns:

-- id - The unique user's ID;
-- login - The unique user's login;
-- name - The user's name;
-- type - The user's role type (which can be "user", "admin", "moderator", etc.).
-- The query you have access to gathers some information about the users who have the "user" type. You don't want to get caught, so you want to carefully update it so that the query will return the records of all existing types.

-- Your task is to update the existing query. Note: You should add something to the query, but don't rewrite it.

-- Example

-- For the given table users

-- id	login	name	type
-- 1	Ann92	Ann	user
-- 2	Bob88	Bob	user
-- 3	Carol412	Carol	admin
-- 4	Deril39	Deril	admin
-- 5	EvaGrin	Eva	user
-- the existing query returns the following table:

-- id	login	name
-- 1	Ann92	Ann
-- 2	Bob88	Bob
-- 5	EvaGrin	Eva
-- but the updated query should return the following one:

-- id	login	name
-- 1	Ann92	Ann
-- 2	Bob88	Bob
-- 3	Carol412	Carol
-- 4	Deril39	Deril
-- 5	EvaGrin Eva


CREATE PROCEDURE solution()
    SELECT id,login,name
    FROM users
    WHERE type='user'
    UNION (SELECT id, login,name FROM users WHERE type<>'user')
    ORDER BY id



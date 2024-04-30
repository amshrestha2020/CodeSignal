-- You work for an online store in which each item put up for sale gets a unique randomly generated id.

-- These item ids are stored in the itemIds table with only one column:

-- id: unique id of an item.
-- However, this system proved to be not very convenient to use in a number of queries that required consecutive ids. To solve this problem, you decided to generate new ids for the items using the following algorithm: the item with the smallest id would get 1 as a new id, the second smallest would get 2, and so on.

-- Given the itemIds table, write a select statement which returns two columns: oldId and newId. The first column should contain the old item id, and the second one should contain the new id generated as described above. The output should be sorted by the newId in ascending order.

-- Example

-- For the following table itemIds

-- id
-- 1
-- 12
-- 23
-- 42
-- 49
-- 678
-- 3242
-- 9320
-- 67867
-- 84523
-- the output should be

-- oldId	newId
-- 1	1
-- 12	2
-- 23	3
-- 42	4
-- 49	5
-- 678	6
-- 3242	7
-- 9320	8
-- 67867	9
-- 84523	10


CREATE PROCEDURE solution()
BEGIN
	/* Write your SQL here. Terminate each statement with a semicolon. */
	SELECT id AS oldId, ROW_NUMBER() OVER (ORDER BY id) AS newId
    FROM itemIds
    ORDER BY newId;
END
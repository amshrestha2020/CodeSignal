-- You recently started working in the IT department of a large store. You were put in charge of the inventory database availableItems, which has the following structure:

-- id: unique item ID;
-- item_name: the name of the item;
-- item_type: the type of the item.
-- Note that it is possible for items that are of different types to have the same names.

-- One of the most common operations performed on this database is querying the number of specific items available at the store. Since the database is quite large, queries of this type can take up too much time. You have decided to start analyzing this problem by counting the number of each available item.

-- Given the availableItems table, write a select statement which returns the following three columns: item_name, item_type and item_count, containing the names of the items, their types, and the amount of those items, respectively. The output should be sorted in ascending order by item type, with items of the same type sorted in ascending order by their names.

-- Example

-- For the following table availableItems

-- id	item_name	item_type
-- 1	SafeDisk 4GB	USB drive
-- 2	SafeDisk 8GB	USB drive
-- 3	Cinco 50-Pack	DVD
-- 4	SafeDisk 4GB	Memory card
-- 5	SafeDisk 8GB	Memory card
-- 6	Cinco 30-Pack	DVD
-- 7	SafeDisk 4GB	Memory card
-- 8	SafeDisk 4GB	Memory card
-- 9	DiskHolder	Misc
-- 10	Cinco 50-Pack	DVD
-- 11	SafeDisk 4GB	USB drive
-- 12	DiskCleaner Pro	Misc
-- the output should be

-- item_name	item_type	item_count
-- Cinco 30-Pack	DVD	1
-- Cinco 50-Pack	DVD	2
-- SafeDisk 4GB	Memory card	3
-- SafeDisk 8GB	Memory card	1
-- DiskCleaner Pro	Misc	1
-- DiskHolder	Misc	1
-- SafeDisk 4GB	USB drive	2
-- SafeDisk 8GB	USB drive	1


CREATE PROCEDURE solution()
BEGIN
	/* Write your SQL here. Terminate each statement with a semicolon. */
	SELECT
    item_name,
    item_type,
    COUNT(*) AS item_count
FROM availableItems
GROUP BY item_name, item_type
ORDER BY item_type ASC, item_name ASC;

END
-- Implement the missing code, denoted by ellipses. You may not modify the pre-existing code.
-- You're writing queries for the database of an online store.

-- You were given access to the orders and item_prices tables, which have the following structures:

-- orders:
-- id: the unique order ID;
-- buyer: the buyer's name;
-- items: the ID of the items included in the order, separated by a semicolon ;. Contains at least one ID.
-- item_prices:
-- id: the unique item ID;
-- price: the price of the item.
-- Given the orders and item_prices tables, write a function that will calculate each order's total price, given the purchased items as a string of item IDs separated by semicolons.

-- Example

-- The following tables orders

-- id	buyer	items
-- 1	Justin Penrose	1
-- 2	Bertha Neiman	1;2;14
-- 3	John Doe	1;14;15
-- and item_prices

-- id	price
-- 1	100
-- 2	200
-- 3	500
-- 4	250
-- 14	50
-- 15	75
-- 16	100
-- the output should be

-- id	buyer	total_price
-- 1	Justin Penrose	100
-- 2	Bertha Neiman	350
-- 3	John Doe	225


DROP FUNCTION IF EXISTS get_total;
CREATE FUNCTION get_total(items VARCHAR(45)) RETURNS INT DETERMINISTIC
BEGIN
    SET @next = '';
  SET @nextLen = 0;
  SET @ret = 0;
    iterator:
LOOP
  IF LENGTH(items) = 0 OR items IS NULL THEN
    LEAVE iterator;
  END IF;

  SET @next = SUBSTRING_INDEX(items,';',1);
  SET @nextLen = LENGTH(@next);
  
  SELECT @ret+price INTO @ret FROM item_prices WHERE id=@next LIMIT 1;
  
  SET items = INSERT(items,1,@nextLen + 1,'');
END LOOP;
  RETURN @ret;
END;

CREATE PROCEDURE orderPrices()
BEGIN
    SELECT id, buyer, get_total(items) AS total_price
    FROM orders
    ORDER BY id;
END;

CREATE PROCEDURE solution()
BEGIN
    SELECT id, buyer, get_total(items) AS total_price
    FROM orders
    ORDER BY id;
END;

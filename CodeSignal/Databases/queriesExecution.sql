-- You're working at a company that sells handmade toys. You're supposed to write a monthly report for your managers about how the company is doing. It takes a lot of time to create these reports manually, so you decided to write a function that will make the process easier.

-- Information for your reports is given in three tables:

-- orders (information about the orders made throughout the month):
-- order_id: the unique order ID;
-- order_type: either "Buy" or "Sell";
-- date_placed: the date the order was made;
-- order_qty: the quantity of ordered items;
-- order_price: the price of the order;
-- execution (information about executed orders):
-- execution_id: the unique execution ID;
-- order_id: foreign key referencing orders.order_id;
-- execution_date: the date of the execution;
-- execution_qty: the quantity of bought or sold items;
-- execution_price: the cost of the execution;
-- queries (queries which results should be in the reports):
-- query_name: the name of the query;
-- code: the code of the query that should be executed; it's guaranteed that each code returns exactly one value.
-- In order to prepare the required values for your next report, you should create a new table with columns query_name and val. For each query_name, the result of the executed query should be stored in the respective val column. The table should be sorted by query_name in ascending order.

-- Example

-- For the following tables orders:

-- order_id	order_type	date_placed	order_qty	order_price
-- 1	Buy	2014-03-15	5	50
-- 2	Buy	2014-02-03	15	23
-- 3	Sell	2014-01-16	45	2
-- 4	Sell	2014-01-17	10	7
-- execution:

-- execution_id	order_id	execution_date	execution_qty	execution_price
-- 1	1	2014-03-16	2	49
-- 2	1	2014-03-17	3	51
-- 3	2	2014-02-03	15	22
-- 4	3	2014-01-17	45	2
-- and queries:

-- query_name	code
-- AVG_EXEC_PRICE	SELECT AVG(execution_price) FROM `execution`
-- COUNT_EXECUTIONS	SELECT COUNT(execution_id) FROM `execution`
-- MIN_ORDER_DATE	SELECT MIN(date_placed) FROM `orders`
-- SUM_ORD_QTY	SELECT SUM(order_qty) FROM `orders`
-- the output should be
-- query_name	val
-- AVG_EXEC_PRICE	31.000000000
-- COUNT_EXECUTIONS	4
-- MIN_ORDER_DATE	2014-01-16
-- SUM_ORD_QTY	75



CREATE PROCEDURE solution()
BEGIN
	/* Write your SQL here. Terminate each statement with a semicolon. */
    DECLARE done INT DEFAULT 0;
    DECLARE query_name_var VARCHAR(100);
    DECLARE query_code_var TEXT;
    DECLARE query_result VARCHAR(100);

    -- Declare cursor to iterate over queries
    DECLARE cur CURSOR FOR SELECT query_name, code FROM queries;
    
    -- Declare continue handler to exit loop when no more rows
    DECLARE CONTINUE HANDLER FOR NOT FOUND SET done = 1;
	
	DROP TEMPORARY TABLE IF EXISTS report;

    -- Create temporary table to store report values
    CREATE TEMPORARY TABLE IF NOT EXISTS report (
        query_name VARCHAR(100),
        val VARCHAR(100)
    );

    -- Open cursor
    OPEN cur;
    read_loop: LOOP
      FETCH cur INTO query_name_var, query_code_var;
      IF done THEN
        LEAVE read_loop;
      END IF;

      SET @execq=CONCAT("INSERT INTO report values(", "'", query_name_var, "'", ",(", query_code_var, "));");

      PREPARE stmt FROM @execq;
      EXECUTE stmt; 
      DEALLOCATE PREPARE stmt;
    END LOOP;
    CLOSE cur;
    
    SELECT query_name, val FROM report;
END


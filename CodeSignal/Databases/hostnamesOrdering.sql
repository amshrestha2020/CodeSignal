-- Yesterday you wrote down the links for some resources that you are going to use as references in your academic paper, and now you want to sort them. You didn't bother to write down the entire link for any of them, so all you have is a bunch of unique hostnames.

-- You stored the information about these hostnames in the table hostnames, which has the structure:

-- id: the unique hostname id;
-- hostname: the unique hostname.
-- Each hostname contain several domains and can be written in the format hostname = domain1.domain2. .... To sort the hostnames, you've decided that hostname A should go before hostname B in the sorted list if its reversed list of domains is lexicographically smaller than the reversed list of B's domains.

-- Given the table hostnames, write a select statement as follows: The output should have columns id and hostname, and its values should be ordered as described above. It is guaranteed that all the hostnames are different and that there are no more than 3 domains in each hostname.

-- Example

-- For the following table hostnames

-- id	hostname
-- 1	workbench.mysql.com
-- 2	codesignal.slack.com
-- 3	codesignal.com
-- 4	snarknews.info
-- 5	sololearn.com
-- 6	dev.mysql.com
-- the output should be

-- id	hostname
-- 3	codesignal.com
-- 6	dev.mysql.com
-- 1	workbench.mysql.com
-- 2	codesignal.slack.com
-- 5	sololearn.com
-- 4	snarknews.info


CREATE PROCEDURE solution()
BEGIN
	/* Write your SQL here. Terminate each statement with a semicolon. */
	SELECT id, hostname
    FROM hostnames
    ORDER BY 
      SUBSTRING_INDEX(CONCAT(' .',hostname), '.', -1),
      SUBSTRING_INDEX(CONCAT(' ..',hostname), '.', -2),
	  hostname ASC;
END
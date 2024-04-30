-- Your company is planning to expand internationally very soon. You have been tasked with preparing a report on foreign markets and potential competitors.

-- After some investigation, you've created a database containing a foreignCompetitors table, which has the following structure:

-- competitor: the name of the competitor;
-- country: the country in which the competitor is operating.
-- In your report, you need to include the number of competitors per country and an additional row at the bottom that contains a summary: ("Total:", total_number_of_competitors)

-- Given the foreignCompetitors table, compose the resulting table with two columns: country and competitors. The first column should contain the country name, and the second column should contain the number of competitors in this country. The table should be sorted by the country names in ascending order. In addition, it should have an extra row at the bottom with the summary, as described above.

-- Example

-- For the following table foreignCompetitors

-- competitor	country
-- Acme Corp	USA
-- GLOBEX	USA
-- Openmedia	France
-- K-bam	USA
-- Hatdrill	UK
-- Hexgreen	Germany
-- D-ranron	France
-- Faxla	Spain
-- the output should be

-- country	competitors
-- France	2
-- Germany	1
-- Spain	1
-- UK	1
-- USA	3
-- Total:	8


CREATE PROCEDURE solution()
BEGIN
	/* Write your SQL here. Terminate each statement with a semicolon. */
	SELECT IFNULL(country, 'Total:') as country, COUNT(competitor) as competitors
    FROM foreignCompetitors
    GROUP BY country WITH ROLLUP;


END
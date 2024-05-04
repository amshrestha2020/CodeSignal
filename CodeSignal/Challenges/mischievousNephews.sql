CREATE PROCEDURE solution()
BEGIN
	/* Write your SQL here. Terminate each statement with a semicolon. */
	
    SELECT
    CASE
        WHEN weekday = 0 THEN 'Huey'
        WHEN weekday = 1 THEN 'Dewey'
        WHEN weekday = 2 THEN 'Louie'
    END AS name,
    mischief_date,
    author,
    title
FROM your_table_name
WHERE author IN ('Huey', 'Dewey', 'Louie');

END
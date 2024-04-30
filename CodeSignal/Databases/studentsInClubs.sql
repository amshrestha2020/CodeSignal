-- Implement the missing code, denoted by ellipses. You may not modify the pre-existing code.
-- At the beginning of this academic year you composed a list of clubs and a list of their members. The gathered information is stored in your local database in two tables that have the following structures:

-- clubs
-- id: unique club id;
-- name: club name;
-- students
-- id: unique student id;
-- name: student name;
-- club_id: id of the club the student joined.
-- Each student can be a member only of a single club, and it is prohibited to drop a club until the year is over. However, several clubs were closed due to low attendance, and you need to update your database to reflect that. You have already updated the clubs table, and now the students table should be updated as well.

-- Given the clubs and students tables, return a table containing the records from students that have club_id equal to some id of clubs. The table should be sorted by students' ids.

-- Example

-- For the following table students

-- id	name	club_id
-- 3	Richard Gear	23
-- 6	Jennifer Offencerence	11
-- 14	Obiten Kenobi	87
-- 36	Closece	87
-- and clubs

-- id	name
-- 23	Theater club
-- 64	Soccer club
-- 87	Glee club
-- the output should be

-- id	name	club_id
-- 3	Richard Gear	23
-- 14	Obiten Kenobi	87
-- 36	Closece	87

CREATE PROCEDURE solution()
    SELECT * FROM students
    WHERE EXISTS (
        SELECT 1
        FROM clubs
        WHERE clubs.id = students.club_id
    )
    ORDER BY students.id;

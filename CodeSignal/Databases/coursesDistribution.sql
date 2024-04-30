-- Implement the missing code, denoted by ellipses. You may not modify the pre-existing code.
-- You work with a professor of applied mathematics and informatics to create and distribute this year's plan of courses for students.
-- You were almost finished when you noticed that a couple of fixes yet need to be done. There are courses which names' are marked as '-toremove', so you decided to remove them permanently. Prior to removing them, you'd like to make sure that deleting a course would also remove it from all the related tables automatically.

-- All courses are stored in courses table that has the following structure:

-- id: unique id of the course;
-- name: unique name of the course that may end with '-toremove', which means that the course is about to be removed;
-- description: description of the course.
-- There are also groupcourses and groupexams tables which represent courses assigned to groups and examination dates of courses for each group, respectively. Here are their structures:

-- groupcourses:
-- group_id: group id;
-- course_id: course id;
-- groupexams:
-- date: the date of the exam;
-- group_id: id of the group taking the exam;
-- course_id: id of the course.
-- Given courses, groupcourses and groupexams tables you need to properly set up foreign keys, so that after a record is deleted from the courses table, records that correspond to the deleted course are also deleted from groupcourses and groupexams. Please note that groupexams can only contain pairs from groupcourses and there can be multiple exam dates for the same group_id, course_id combination. It is guaranteed that adding correct foreign keys won't raise any errors.

-- Example

-- For the following tables courses

-- id	name	description
-- 1	Linear algebra	Basis of matrix theory and linear algebra
-- 2	Geometry	NULL
-- 3	Determinants and matrices	NULL
-- 4	Matlab-toremove	Matlab 7
-- groupcourses

-- group_id	course_id
-- 1	1
-- 1	2
-- 1	3
-- 2	1
-- 2	4
-- and groupexams

-- date	group_id	course_id
-- 2010-01-10	1	1
-- 2010-01-11	1	2
-- 2010-01-12	2	4
-- the final result should be

-- group_id	course_id
-- 1	1
-- 1	2
-- 1	3
-- 2	1


CREATE PROCEDURE solution()
BEGIN
    ALTER TABLE groupcourses ADD FOREIGN KEY (course_id)
    REFERENCES courses(id) ON DELETE CASCADE;

    ALTER TABLE groupexams ADD FOREIGN KEY (course_id)
    REFERENCES courses(id) ON DELETE CASCADE;

    DELETE FROM courses WHERE name LIKE '%-toremove';


    SELECT group_id, course_id
      FROM groupcourses
     UNION
    SELECT group_id, course_id
      FROM groupexams
     ORDER BY group_id, course_id;
END
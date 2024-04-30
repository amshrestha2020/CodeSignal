-- At the end of every semester your professor for "Introduction to Databases" saves the exam results of every student in a simple database system. In the database table Grades, there are five columns:

-- Name: the name of the student;
-- ID: the student's ID number (a 5 byte positive integer);
-- Midterm1: the result of the first midterm out of 100 points;
-- Midterm2: the result of the second midterm out of 100 points;
-- Final: the result of the final exam, this time out of a possible 200 points.
-- According to school policy, there are three possible ways to evaluate a grade:

-- Option 1: Grade = 0.25 * Midterm1 + 0.25 * Midterm2 + 0.5 * Final;
-- Option 2: Grade = 0.5 * Midterm1 + 0.5 * Midterm2;
-- Option 3: Grade = Final.
-- Each student's final grade comes from the option that works the best for that student.

-- As a Teaching Assistant (TA), you need to query the name and id of all the students whose best grade comes from Option 3, sorted based on the first 3 characters of their name. If the first 3 characters of two names are the same, then the student with the lower ID value comes first.

CREATE PROCEDURE solution()
BEGIN
	/* Write your SQL here. Terminate each statement with a semicolon. */
SELECT Name, ID FROM Grades WHERE Final > (Midterm1 + Midterm2)/2 AND Final > 
((Midterm1+Midterm2)/2 +Final)/2 ORDER BY SUBSTRING(Name, 1, 3), ID ASC;
END



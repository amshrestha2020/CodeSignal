-- Implement the missing code, denoted by ellipses. You may not modify the pre-existing code.
-- Your professor gave the class a bonus task: Write a program that will check the answers for the latest test. The program will be given a table answers with the following columns:

-- id - the unique ID of the question;
-- correct_answer - the correct answer to the question, given as a string;
-- given_answer - the answer given to the question, which can be NULL.
-- Your task is to return the table with a column id and a column checks, where for each answers id the following string should be returned:

-- "no answer" if the given_answer is empty;
-- "correct" if the given_answer is the same as the correct_answer;
-- "incorrect" if the given_answer is not empty and is incorrect.
-- Order the records in the answer table by id.


CREATE PROCEDURE solution()
    SELECT id, IF ( given_answer IS NULL, 'no answer', IF ( given_answer =correct_answer, 'correct', 'incorrect') ) AS checks
    FROM answers
    ORDER BY id;

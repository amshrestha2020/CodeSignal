-- Implement the missing code, denoted by ellipses. You may not modify the pre-existing code.
-- You are the chairman of your university's drawing club, which isn't doing very well right now. The club meets two times a week to exchange drawing advice, talk about new techniques, and draw something together. But the members are starting to get bored during these meetings, so you've decided to add an additional activity to the routine.

-- In order to do this, you decided to collect information about the students, which is now stored in the table people_interests, which has the following columns:

-- name - the unique name of a person;
-- interests - the set of interests or hobbies this person has, given as a comma-joined string. This column has datatype set('reading','sports','swimming','drawing','writing','acting','cooking','dancing','fishkeeping','juggling','sculpting','videogaming').
-- This information gave you the idea that reading might be an interesting theme for the next meeting, so you announced that the next meeting will be reading-related. Now you're interested in the number of members that will come.

-- Given the people_interests table, find the people who will attend the next meeting, i.e. those who are fond of both drawing and reading. The resulting table should consist of a single name column, and the records should be sorted by people's names.

-- Example

-- For given table people_interests

-- name	interests
-- August	cooking,juggling
-- Buddy	reading,swimming,drawing,acting,dancing,videogaming
-- David	juggling,sculpting
-- Dennis	swimming,cooking,fishkeeping
-- James	reading,drawing
-- the output should be

-- name
-- Buddy
-- James


CREATE PROCEDURE solution()
    SELECT name
    FROM people_interests
    WHERE interests & 1 AND interests & 8
    ORDER BY name

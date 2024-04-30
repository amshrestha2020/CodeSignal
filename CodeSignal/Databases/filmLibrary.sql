-- You have a very big personal library of movies. You also have information about these movies stored in three tables - movies, starring_actors, and actor_ages. These tables have the following structures:

-- movies:
-- movie: the unique name of the movie;
-- genre: the genre of the movie.
-- starring_actors:
-- id: the unique ID of the record;
-- movie_name: the name of the movie;
-- actor: the unique actor who stars in the movie. (You've made the decision to only add only one movie for each actor, the one in which they had the best role.)
-- actor_ages:
-- actor: the unique name of the actor;
-- age: the actor's age.
-- You've noticed that an actor usually only acts in the movies from one genre. And you believe that the older an actor is, the better they perform.

-- Now you don't know what to watch! So you decided to write a select statement that returns a list of actors, from oldest to youngest (if actors are the same age, sort them by name), who star in the movies in your favorite genre. (Your favorite genre is the most common one in your list of the movies, and it's guaranteed that only one such genre exists.) So now you can find the movies these actors star in, and there is a strong chance that these movies will be in your favorite genre.

-- Example

-- For the following tables movies

-- movie	genre
-- Don't Breathe	crime movie
-- Drive	crime movie
-- Enemy	thriller
-- Mulholland Drive	mystery
-- Nocturnal Animals	thriller
-- The Neon Demon	thriller
-- starring_actors:

-- id	movie_name	actor
-- 1	Drive	Ryan Gosling
-- 2	Drive	Carey Mulligan
-- 3	Don't Breathe	Dylan Minnette
-- 4	Enemy	Jake Gyllenhaal
-- 5	Enemy	Sarah Gadon
-- 6	Mulholland Drive	Naomi Watts
-- 7	Mulholland Drive	Laura Harring
-- 8	Nocturnal Animals	Amy Adams
-- 9	Nocturnal Animals	Aaron Taylor-Johnson
-- 10	Nocturnal Animals	Michael Shannon
-- 11	The Neon Demon	Elle Fanning
-- 12	The Neon Demon	Keanu Reeves
-- and actor_ages:

-- actor	age
-- Aaron Taylor-Johnson	26
-- Amy Adams	42
-- Carey Mulligan	31
-- Dylan Minnette	19
-- Elle Fanning	18
-- Jake Gyllenhaal	36
-- Keanu Reeves	52
-- Laura Harring	52
-- Michael Shannon	42
-- Naomi Watts	48
-- Ryan Gosling	36
-- Sarah Gadon	29
-- the output should be
-- actor	age
-- Keanu Reeves	52
-- Amy Adams	42
-- Michael Shannon	42
-- Jake Gyllenhaal	36
-- Sarah Gadon	29
-- Aaron Taylor-Johnson	26
-- Elle Fanning	18
-- As you can see in the first table, the most common genre is "thriller" - it appears 3 times out of 6. These 3 movies are "Enemy", "Nocturnal Animals", and "The Neon Demon". The actors starring in these movies are presented in the resulting table, sorted by ages.



CREATE PROCEDURE solution()
BEGIN
	/* Write your SQL here. Terminate each statement with a semicolon. */
	SELECT a.actor, aa.age
FROM starring_actors a
JOIN movies m ON a.movie_name = m.movie
JOIN actor_ages aa ON a.actor = aa.actor
WHERE m.genre = (
    SELECT genre
    FROM movies
    GROUP BY genre
    ORDER BY COUNT(*) DESC
    LIMIT 1
)
ORDER BY aa.age DESC, a.actor;

END
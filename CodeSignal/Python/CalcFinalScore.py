# Implement the missing code, denoted by ellipses. You may not modify the pre-existing code.
# You are working on a revolutionary video game. This game will consist of several levels, and on each level the player will be able to collect bonuses. For each passed level the player will thus get some score, determined by the number of collected bonuses.

# Player's final score is decided by the number of completed levels and scores obtained on each of them. The final score is calculated as the sum of squares of n maximum scores obtained. If the number of completed levels is less than n, the score is calculated as the sum of squared scores for each level, and final result is divided by 5 as a penalty (the result is rounded down to the nearest integer).

# Given the list of scores the player got for completed levels and the number n that determines the number of levels you have to pass to avoid being penalized, return the player's final game score.

# Example

# For scores = [4, 2, 4, 5] and n = 3,
# the output should be
# solution(scores, n) = 57.

# 52 + 42 + 42 = 57.

# For scores = [4, 2, 4, 5] and n = 5,
# the output should be
# solution(scores, n) = 12.

# (42 + 22 + 42 + 52) / 5 = 61 / 5 ≈ 12.


def solution(scores, n):
    gen = iter(a**2 for a in sorted(scores)[-n:])

    res = 0
    try:
        for _ in range(n):
            res += next(gen)
    except StopIteration:
        res //= 5

    return res


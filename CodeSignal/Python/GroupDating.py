# Implement the missing code, denoted by ellipses. You may not modify the pre-existing code.
# You're organizing a group dating activity for cats, i.e. a meeting where an equal number of male and female cats get together. For each cat you calculate their nature value, an integer that describes the cat's spirit. When a male and a female cat with the same nature value see each other, they become connected and happily walk out together.

# You've just started another group dating, and placed the cats in front of one another so that the ith male is sitting across the ith female. What cats will remain at their places, assuming that the pairs of cats sitting in front of each other and having the same nature values will walk out?

# Example

# For male = [5, 28, 14, 99, 17] and
# female = [5, 14, 28, 99, 16],
# the output should be
# solution(male, female) = [[28, 14, 17], [14, 28, 16]].

# Pairs of cats at positions 0 and 3 (0-based) have the same nature values, so they will leave the meeting


def solution(male, female):
    return [[m for m, f in zip(male, female) if m != f], [f for m, f in zip(male, female) if m != f]]


# Implement the missing code, denoted by ellipses. You may not modify the pre-existing code.
# You found your old bike in the attic, and would love to refresh your childhood memories and give it a ride. Unfortunately there is a chain lock on the bike, and the code is a permutation of a set of distinct numbers. Of course, you don't remember it after all these years.

# You do remember, however, that the last time you picked up your bike you also couldn't remember the code, so had to run over all possible numbers permutations. Being a programmer, you tried them in the lexicographical order. It took you a couple of days, and in the first day you managed to check k - 1 permutations.

# Now that you need to open the lock again, you can start checking the permutations from the kth one. Given the list of numbers, return the kth (1-based) permutation that you should begin with.

# Example

# For numbers = [1, 2, 3, 4, 5] and k = 4, the output should be
# solution(numbers, k) = [1, 2, 4, 5, 3].

# Here are the first 4 permutations:

# [1, 2, 3, 4, 5]
# [1, 2, 3, 5, 4]
# [1, 2, 4, 3, 5]
# [1, 2, 4, 5, 3]


from itertools import permutations, islice

def solution(numbers, k):
    return next(islice(permutations(numbers), k-1, None))


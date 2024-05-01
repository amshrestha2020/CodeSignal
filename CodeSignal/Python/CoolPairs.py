# Implement the missing code, denoted by ellipses. You may not modify the pre-existing code.
# A pair of numbers is considered to be cool if their product is divisible by their sum. More formally, a pair (i, j) is cool if and only if (i * j) % (i + j) = 0.

# Given two lists a and b, find cool pairs with the first number in the pair from a, and the second one from b. Return the number of different sums of elements in such pairs.

# Example

# For a = [4, 5, 6, 7, 8] and b = [8, 9, 10, 11, 12],
# the output should be
# solution(a, b) = 2.

# There are three cool pairs that can be formed from these arrays: (4, 12), (6, 12) and (8, 8). Their respective sums are 16, 18 and 16, which means that there are just 2 different sums: 16 and 18. Thus, the output should be equal to 2.


def solution(a, b):
    uniqueSums = {i+j for i in a for j in b if (i*j) % (i+j) == 0}
    return len(uniqueSums)

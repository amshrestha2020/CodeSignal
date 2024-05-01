# Implement the missing code, denoted by ellipses. You may not modify the pre-existing code.
# You need to sum up a bunch of fractions that have different denominators. In order to do this, you need to find the least common denominator of all the fractions. As a professional programmer, you know that the least common denominator is in fact their LCM.

# For the given list of denominators, find the least common denominator by finding their LCM.

# Example

# For denominators = [2, 3, 4, 5, 6], the output should be
# solution(denominators) = 60.

from math import gcd

def solution(denominators):
    return functools.reduce(lambda x, y: x * y // gcd(x, y), denominators)

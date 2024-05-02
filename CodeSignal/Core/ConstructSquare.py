# Given a string consisting of lowercase English letters, find the largest square number which can be obtained by reordering the string's characters and replacing them with any digits you need (leading zeros are not allowed) where same characters always map to the same digits and different characters always map to different digits.

# If there is no solution, return -1.

# Example

# For s = "ab", the output should be
# solution(s) = 81.
# The largest 2-digit square number with different digits is 81.
# For s = "zzz", the output should be
# solution(s) = -1.
# There are no 3-digit square numbers with identical digits.
# For s = "aba", the output should be
# solution(s) = 900.
# It can be obtained after reordering the initial string into "baa" and replacing "a" with 0 and "b" with 9.

import math


def solution(s):
    c = sorted([s.count(x) for x in set(s)])
    
    # generator largest possible number based on string length
    mx = 0
    for i in range(len(s)):
        mx += 9*10**i
        
    # decrement from largest possible number and check squares
    while mx > 0:
        # is square
        if mx == math.isqrt(mx) ** 2:
            # count how often each digit occurs
            print(mx)
            cc = [str(mx).count(x) for x in set(str(mx))]
            # if the number of digits and number of character occurrences matches
            if sorted(cc) == c:
               return mx
        # at the end to catch the i-digits strings ;-)
        mx -= 1
                       
    return -1
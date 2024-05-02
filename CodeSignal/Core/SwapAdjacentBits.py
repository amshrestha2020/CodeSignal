# Implement the missing code, denoted by ellipses. You may not modify the pre-existing code.
# You're given an arbitrary 32-bit integer n. Take its binary representation, split bits into it in pairs (bit number 0 and 1, bit number 2 and 3, etc.) and swap bits in each pair. Then return the result as a decimal number.

# Example

# For n = 13, the output should be
# solution(n) = 14.

# 1310 = 11012 ~> {11}{01}2 ~> 11102 = 1410.

# For n = 74, the output should be
# solution(n) = 133.

# 7410 = 010010102 ~> {01}{00}{10}{10}2 ~> 100001012 = 13310.
# Note the preceding zero written in front of the initial number: since both numbers are 32-bit integers, they have 32 bits in their binary representation. The preceding zeros in other cases don't matter, so they are omitted. Here, however, it does make a difference.


def solution(n):
    return int(''.join([(format(n, '032b'))[i:i+2][::-1] for i in range(0, len(format(n, '032b')), 2)]), 2)

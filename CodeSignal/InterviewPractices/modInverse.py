# We will define the multiplicative inverse n modulo m as an integer ninv such that (n · ninv) % m = 1. We will restrict our attention to the inverses ninv in the interval [o, m-1].

# Note: For a % b, the % sign indicates the modulo operation (i.e., the remainder of dividing a by b).

# Given the numbers n and m, find the multiplicative inverse n modulo m. If no such multiplicative inverse exists, return -1.

# Example

# For n = 4 and m = 15, the output should be
# solution(n, m) = 4.

# 4 · 4 = 16 = 15 · 1 + 1, i.e. (4 · 4) % 15 = 1, so ninv = 4 is correct answer.

# For n = 7 and m = 15, the output should be
# solution(n, m) = 13.

# 7 · 13 = 91 = 15 · 6 + 1, i.e. (7 · 13) % 15 = 1, so ninv = 13 is correct answer.

# For n = 5 and m = 15, the output should be
# solution(n, m) = -1.

# None of numbers 0, 1, ..., 14 are correct.


def solution(n, m):
    def extended_gcd(a, b):
        if a == 0:
            return b, 0, 1
        else:
            g, x, y = extended_gcd(b % a, a)
            return g, y - (b // a) * x, x

    g, x, _ = extended_gcd(n, m)
    if g == 1:
        return x % m
    else:
        return -1

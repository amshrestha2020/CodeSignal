# Find the number of ways to express n as sum of some (at least two) consecutive positive integers.

# Example

# For n = 9, the output should be
# solution(n) = 2.

# There are two ways to represent n = 9: 2 + 3 + 4 = 9 and 4 + 5 = 9.

# For n = 8, the output should be
# solution(n) = 0.

# There are no ways to represent n = 8.\

def solution(n):
    c = 0

    for i in range(1,n):
        s = i
        j = 1

        while s < n:
            s = s + i + j
            j += 1

        if s == n:
            c += 1

    return c

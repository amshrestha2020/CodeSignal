# You are climbing a staircase that has n steps. You can take the steps either 1 or 2 at a time. Calculate how many distinct ways you can climb to the top of the staircase.

# Example

# For n = 1, the output should be
# solution(n) = 1;

# For n = 2, the output should be
# solution(n) = 2.

# You can either climb 2 steps at once or climb 1 step two times.


def solution(n):
    if n <= 2:
        return n
    ways = [0] * (n + 1)
    ways[1] = 1
    ways[2] = 2
    for i in range(3, n + 1):
        ways[i] = ways[i - 1] + ways[i - 2]
    return ways[n]

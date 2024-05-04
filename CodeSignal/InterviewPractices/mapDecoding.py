# A top secret message containing uppercase letters from 'A' to 'Z' has been encoded as numbers using the following mapping:

# 'A' -> 1
# 'B' -> 2
# ...
# 'Z' -> 26
# You are an FBI agent and you need to determine the total number of ways that the message can be decoded.

# Since the answer could be very large, take it modulo 109 + 7.

# Example

# For message = "123", the output should be
# solution(message) = 3.

# "123" can be decoded as "ABC" (1 2 3), "LC" (12 3) or "AW" (1 23), so the total number of ways is 3.


def solution(message):
    mod = 10**9 + 7
    dp = [0] * (len(message) + 1)
    dp[0] = 1
    for i in range(1, len(dp)):
        if message[i - 1] != '0':
            dp[i] += dp[i - 1]
        if i != 1 and '10' <= message[i - 2:i] <= '26':
            dp[i] += dp[i - 2]
        dp[i] %= mod
    return dp[-1]

# Given a sequence of numbers in an array, find the length of its longest increasing subsequence (LIS).
# The longest increasing subsequence is a subsequence of a given sequence in which the subsequence's elements are in strictly increasing order, and in which the subsequence is as long as possible. This subsequence is not necessarily contiguous or unique.

# Example

# For sequence = [1, 231, 2, 4, 89, 32, 12, 234, 33, 90, 34, 100], the output should be
# solution(sequence) = 7.

# The LIS itself is [1, 2, 4, 32, 33, 34, 100]

def solution(sequence):
    dp = [1] * len(sequence)
    for i in range(1, len(sequence)):
        for j in range(i):
            if sequence[i] > sequence[j] and dp[i] < dp[j] + 1:
                dp[i] = dp[j] + 1
    return max(dp)

# You have a 2D binary matrix that's filled with 0s and 1s. In the matrix, find the largest square that contains only 1s and return its area.

# Example

# For

# matrix = [
#     ['1', '0', '1', '1', '1'],
#     ['1', '0', '1', '1', '1'],
#     ['1', '1', '1', '1', '1'],
#     ['1', '0', '0', '1', '0'],
#     ['1', '0', '0', '1', '0']
# ]
# the output should be
# solution(matrix) = 9.


def solution(matrix):
    if not matrix:
        return 0
    m, n = len(matrix), len(matrix[0])
    dp = [[0] * n for _ in range(m)]
    max_side = 0
    for i in range(m):
        for j in range(n):
            if matrix[i][j] == '1':
                if i == 0 or j == 0:
                    dp[i][j] = 1
                else:
                    dp[i][j] = min(dp[i - 1][j], dp[i][j - 1], dp[i - 1][j - 1]) + 1
                max_side = max(max_side, dp[i][j])
    return max_side ** 2

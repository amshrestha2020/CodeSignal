# Note: Try to solve this task in-place (with O(1) additional memory), since this is what you'll be asked to do during an interview.

# You are given an n x n 2D matrix that represents an image. Rotate the image by 90 degrees (clockwise).

# Example

# For

# a = [[1, 2, 3],
#      [4, 5, 6],
#      [7, 8, 9]]
# the output should be

# solution(a) =
#     [[7, 4, 1],
#      [8, 5, 2],
#      [9, 6, 3]]


def solution(matrix):
    n = len(matrix)
    for i in range(n // 2):
        for j in range(i, n - i - 1):
            temp = matrix[i][j]
            matrix[i][j] = matrix[n - j - 1][i]
            matrix[n - j - 1][i] = matrix[n - i - 1][n - j - 1]
            matrix[n - i - 1][n - j - 1] = matrix[j][n - i - 1]
            matrix[j][n - i - 1] = temp
    return matrix

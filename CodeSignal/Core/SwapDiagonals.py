# The longest diagonals of a square matrix are defined as follows:

# the first longest diagonal goes from the top left corner to the bottom right one;
# the second longest diagonal goes from the top right corner to the bottom left one.
# Given a square matrix, your task is to swap its longest diagonals by exchanging their elements at the corresponding positions.

# Example

# For

# matrix = [[1, 2, 3],
#           [4, 5, 6],
#           [7, 8, 9]]
# the output should be

# solution(matrix) = [[3, 2, 1],
#                     [4, 5, 6],
#                     [9, 8, 7]]

def solution(matrix):
    start = 0
    end = len(matrix) - 1

    while end - start >= 1:
        topLeft = matrix[start][start]
        bottomLeft = matrix[end][start]

        matrix[start][start] = matrix[start][end]
        matrix[start][end] = topLeft

        matrix[end][start] = matrix[end][end]
        matrix[end][end] = bottomLeft

        start += 1
        end -= 1

    return matrix

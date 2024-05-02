# The longest diagonals of a square matrix are defined as follows:

# the first longest diagonal goes from the top left corner to the bottom right one;
# the second longest diagonal goes from the top right corner to the bottom left one.
# Given a square matrix, your task is to reverse the order of elements on both of its longest diagonals.

# Example

# For

# matrix = [[1, 2, 3],
#           [4, 5, 6],
#           [7, 8, 9]]
# the output should be

# solution(matrix) = [[9, 2, 7],
#                     [4, 5, 6],
#                     [3, 8, 1]]


def solution(matrix):
    start = 0
    end = len(matrix) - 1

    while end - start >= 1:
        topLeft = matrix[start][start]
        topRight = matrix[start][end]

        matrix[start][start] = matrix[end][end]
        matrix[end][end] = topLeft

        matrix[start][end] = matrix[end][start]
        matrix[end][start] = topRight

        start += 1
        end -= 1

    return matrix

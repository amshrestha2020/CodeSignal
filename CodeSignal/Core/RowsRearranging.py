# Given a rectangular matrix of integers, check if it is possible to rearrange its rows in such a way that all its columns become strictly increasing sequences (read from top to bottom).

# Example

# For

# matrix = [[2, 7, 1], 
#           [0, 2, 0], 
#           [1, 3, 1]]
# the output should be
# solution(matrix) = false;

# For

# matrix = [[6, 4], 
#           [2, 2], 
#           [4, 3]]
# the output should be
# solution(matrix) = true.


def solution(matrix):
    if len(matrix) == 1:
        return True
    rearrange_first_col(matrix)

    for col in range(len(matrix[0])):
        for row in range(1, len(matrix)):
            if matrix[row][col] <= matrix[row - 1][col]:
                return False

    return True

def rearrange_first_col(matrix):
    for i in range(len(matrix)):
        min_value_index = i
        for j in range(i + 1, len(matrix)):
            if matrix[min_value_index][0] > matrix[j][0]:
                min_value_index = j

        swap(i, min_value_index, matrix)

def swap(i, j, array):
    temp = array[i]
    array[i] = array[j]
    array[j] = temp

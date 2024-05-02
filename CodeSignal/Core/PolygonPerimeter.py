# You have a rectangular white board with some black cells. The black cells create a connected black figure, i.e. it is possible to get from any black cell to any other one through connected adjacent (sharing a common side) black cells.

# Find the perimeter of the black figure assuming that a single cell has unit length.

# It's guaranteed that there is at least one black cell on the table.

# Example

# For

# matrix = [[false, true,  true ],
#           [true,  true,  false],
#           [true,  false, false]]
# the output should be
# solution(matrix) = 12.



# For

# matrix = [[true, true,  true],
#           [true, false, true],
#           [true, true,  true]]
# the output should be
# solution(matrix) = 16.

def solution(matrix):
    result = 0

    for row in range(len(matrix)):
        for col in range(len(matrix[0])):
            if matrix[row][col]:
                if col == 0 or not matrix[row][col - 1]:
                    result += 1
                if col == len(matrix[0]) - 1 or not matrix[row][col + 1]:
                    result += 1
                if row == 0 or not matrix[row - 1][col]:
                    result += 1
                if row == len(matrix) - 1 or not matrix[row + 1][col]:
                    result += 1

    return result

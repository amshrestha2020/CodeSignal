# In the popular Minesweeper game you have a board with some mines and those cells that don't contain a mine have a number in it that indicates the total number of mines in the neighboring cells. Starting off with some arrangement of mines we want to create a Minesweeper game setup.

# Example

# For

# matrix = [[true, false, false],
#           [false, true, false],
#           [false, false, false]]
# the output should be

# solution(matrix) = [[1, 2, 1],
#                     [2, 1, 1],
#                     [1, 1, 1]]
# Check out the image below for better understanding:



def solution(matrix):
    max_row = len(matrix)
    max_col = len(matrix[0])
    res = [[0] * max_col for _ in range(max_row)]
    locations = [
        [-1, -1],
        [-1, 0],
        [-1, 1],
        [0, -1],
        [0, 1],
        [1, -1],
        [1, 0],
        [1, 1],
    ]

    for row in range(max_row):
        for col in range(max_col):
            if matrix[row][col]:
                for row_to_add, col_to_add in locations:
                    is_valid_row = 0 <= row + row_to_add < max_row
                    is_valid_col = 0 <= col + col_to_add < max_col
                    if is_valid_row and is_valid_col:
                        res[row + row_to_add][col + col_to_add] += 1

    return res

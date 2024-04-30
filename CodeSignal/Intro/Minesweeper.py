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
    rows = len(matrix)
    cols = len(matrix[0])

    # Create an output matrix filled with zeros
    output = [[0] * cols for _ in range(rows)]

    # Define the neighbors' coordinates
    neighbors = [(i, j) for i in range(-1, 2) for j in range(-1, 2) if i != 0 or j != 0]

    # Iterate through each cell in the matrix
    for i in range(rows):
        for j in range(cols):
            # Check if the current cell contains a mine
            if matrix[i][j]:
                # Update the neighbors' counts
                for ni, nj in neighbors:
                    ni, nj = i + ni, j + nj
                    if 0 <= ni < rows and 0 <= nj < cols:
                        output[ni][nj] += 1

    return output


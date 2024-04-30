# Construct a square matrix with a size N × N containing integers from 1 to N * N in a spiral order, starting from top-left and in clockwise direction.

# Example

# For n = 3, the output should be

# solution(n) = [[1, 2, 3],
#                [8, 9, 4],
#                [7, 6, 5]]



def solution(n):
    # Initialize an empty matrix
    matrix = [[0] * n for _ in range(n)]

    # Define directions: right, down, left, up
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]

    # Initialize variables
    num = 1
    row, col = 0, 0
    direction_index = 0

    # Fill the matrix in a spiral order
    for _ in range(1, n * n + 1):
        matrix[row][col] = num
        num += 1

        # Calculate the next position
        next_row, next_col = row + directions[direction_index][0], col + directions[direction_index][1]

        # Change direction if the next position is out of bounds or already visited
        if 0 <= next_row < n and 0 <= next_col < n and matrix[next_row][next_col] == 0:
            row, col = next_row, next_col
        else:
            # Change direction
            direction_index = (direction_index + 1) % 4
            row, col = row + directions[direction_index][0], col + directions[direction_index][1]

    return matrix


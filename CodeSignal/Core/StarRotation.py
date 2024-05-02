# Consider a (2k+1) × (2k+1) square subarray of an integer integers matrix. Let's call the union of the square's two longest diagonals, middle column and middle row a star. Given the coordinates of the star's center in the matrix and its width, rotate it 45 · t degrees clockwise preserving position of all matrix elements that do not belong to the star.

# Example

# For

# matrix = [[1, 0, 0, 2, 0, 0, 3],
#           [0, 1, 0, 2, 0, 3, 0],
#           [0, 0, 1, 2, 3, 0, 0],
#           [8, 8, 8, 9, 4, 4, 4],
#           [0, 0, 7, 6, 5, 0, 0],
#           [0, 7, 0, 6, 0, 5, 0],
#           [7, 0, 0, 6, 0, 0, 5]]
# width = 7, center = [3, 3], and t = 1, the output should be

# solution(matrix, width, center, t) = [[8, 0, 0, 1, 0, 0, 2],
#                                           [0, 8, 0, 1, 0, 2, 0],
#                                           [0, 0, 8, 1, 2, 0, 0],
#                                           [7, 7, 7, 9, 3, 3, 3],
#                                           [0, 0, 6, 5, 4, 0, 0],
#                                           [0, 6, 0, 5, 0, 4, 0],
#                                           [6, 0, 0, 5, 0, 0, 4]]
# For

# matrix = [[1, 0, 0, 2, 0, 0, 3],
#           [0, 1, 0, 2, 0, 3, 0],
#           [0, 0, 1, 2, 3, 0, 0],
#           [8, 8, 8, 9, 4, 4, 4],
#           [0, 0, 7, 6, 5, 0, 0]]
# width = 3, center = [1, 5], and t = 81, the output should be

# solution(matrix, width, center, t) = [[1, 0, 0, 2, 0, 0, 0],
#                                           [0, 1, 0, 2, 3, 3, 3],
#                                           [0, 0, 1, 2, 0, 0, 0],
#                                           [8, 8, 8, 9, 4, 4, 4],
                                 

def solution(matrix, width, center, t):
    for k in range(t % 8):
        midX, midY = center[0], center[1]
        endX = center[0] + (width - 1) // 2
        endY = center[1] + (width - 1) // 2
        startX = center[0] - (width - 1) // 2
        startY = center[1] - (width - 1) // 2

        for i in range((width - 1) // 2):
            temp = matrix[startX][startY]
            matrix[startX][startY] = matrix[midX][startY]
            matrix[midX][startY] = matrix[endX][startY]
            matrix[endX][startY] = matrix[endX][midY]
            matrix[endX][midY] = matrix[endX][endY]
            matrix[endX][endY] = matrix[midX][endY]
            matrix[midX][endY] = matrix[startX][endY]
            matrix[startX][endY] = matrix[startX][midY]
            matrix[startX][midY] = temp

            startX += 1
            startY += 1
            endX -= 1
            endY -= 1

    return matrix

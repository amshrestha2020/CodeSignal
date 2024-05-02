# Given a rectangular matrix containing only digits, calculate the number of different 2 × 2 squares in it.

# Example

# For

# matrix = [[1, 2, 1],
#           [2, 2, 2],
#           [2, 2, 2],
#           [1, 2, 3],
#           [2, 2, 1]]
# the output should be
# solution(matrix) = 6.

# Here are all 6 different 2 × 2 squares:

# 1 2
# 2 2
# 2 1
# 2 2
# 2 2
# 2 2
# 2 2
# 1 2
# 2 2
# 2 3
# 2 3
# 2 1

def solution(matrix):
    diffSquares = set()
    
    # Check all squares
    for i in range(len(matrix) - 1): 
        for j in range(len(matrix[0]) - 1):
            currSquare = (matrix[i][j], matrix[i+1][j], matrix[i][j+1], matrix[i+1][j+1])
            diffSquares.add(currSquare)
    
    return len(diffSquares)

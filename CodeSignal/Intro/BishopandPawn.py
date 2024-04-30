# Given the positions of a white bishop and a black pawn on the standard chess board, determine whether the bishop can capture the pawn in one move.

# The bishop has no restrictions in distance for each move, but is limited to diagonal movement. Check out the example below to see how it can move:


# Example

# For bishop = "a1" and pawn = "c3", the output should be
# solution(bishop, pawn) = true.



# For bishop = "h1" and pawn = "h3", the output should be
# solution(bishop, pawn) = false.



def solution(bishop, pawn):
    # Extract row and column indices for both bishop and pawn
    b_row, b_col = ord(bishop[0]) - ord('a') + 1, int(bishop[1])
    p_row, p_col = ord(pawn[0]) - ord('a') + 1, int(pawn[1])

    # Check if the absolute difference in row and column indices is the same
    return abs(b_row - p_row) == abs(b_col - p_col)


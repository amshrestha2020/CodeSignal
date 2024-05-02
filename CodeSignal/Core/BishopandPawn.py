# Given the positions of a white bishop and a black pawn on the standard chess board, determine whether the bishop can capture the pawn in one move.

# The bishop has no restrictions in distance for each move, but is limited to diagonal movement. Check out the example below to see how it can move:


# Example

# For bishop = "a1" and pawn = "c3", the output should be
# solution(bishop, pawn) = true.



# For bishop = "h1" and pawn = "h3", the output should be
# solution(bishop, pawn) = false.



def solution(bishop, pawn):
    # Calculate the absolute difference in file (column) and rank (row)
    file_diff = abs(ord(bishop[0]) - ord(pawn[0]))
    rank_diff = abs(int(bishop[1]) - int(pawn[1]))
    
    # If the absolute differences are equal, the bishop can capture the pawn
    return file_diff == rank_diff

# Test cases
print(solution("a1", "c3"))  # Output: True
print(solution("h1", "h3"))  # Output: False

# Given two cells on the standard chess board, determine whether they have the same color or not.

# Example

# For cell1 = "A1" and cell2 = "C3", the output should be
# solution(cell1, cell2) = true.



# For cell1 = "A1" and cell2 = "H3", the output should be
# solution(cell1, cell2) = false.

def solution(cell1, cell2):
    # Extract row and column numbers from cell coordinates
    row1, col1 = ord(cell1[0]) - ord('A') + 1, int(cell1[1])
    row2, col2 = ord(cell2[0]) - ord('A') + 1, int(cell2[1])
    
    # Check if the sum of row and column indices is even or odd
    return (row1 + col1) % 2 == (row2 + col2) % 2


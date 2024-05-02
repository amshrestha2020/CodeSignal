# Given a position of a knight on the standard chessboard, find the number of different moves the knight can perform.

# The knight can move to a square that is two squares horizontally and one square vertically, or two squares vertically and one square horizontally away from it. The complete move therefore looks like the letter L. Check out the image below to see all valid moves for a knight piece that is placed on one of the central squares.



# Example

# For cell = "a1", the output should be
# solution(cell) = 2.



# For cell = "c2", the output should be
# solution(cell) = 6.


def solution(cell):
    # Convert the cell coordinates to integers
    column = ord(cell[0]) - ord('a') + 1
    row = int(cell[1])
    
    # Define the possible moves for a knight
    moves = [(2, 1), (2, -1), (-2, 1), (-2, -1), (1, 2), (-1, 2), (1, -2), (-1, -2)]
    
    # Count the number of valid moves
    count = 0
    for move in moves:
        new_column = column + move[0]
        new_row = row + move[1]
        # Check if the new position is within the board
        if 1 <= new_column <= 8 and 1 <= new_row <= 8:
            count += 1
    
    return count

# Test cases
print(solution("a1"))  # Output: 2
print(solution("c2"))  # Output: 6

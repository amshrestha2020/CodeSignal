# Given a position of a knight on the standard chessboard, find the number of different moves the knight can perform.

# The knight can move to a square that is two squares horizontally and one square vertically, or two squares vertically and one square horizontally away from it. The complete move therefore looks like the letter L. Check out the image below to see all valid moves for a knight piece that is placed on one of the central squares.



# Example

# For cell = "a1", the output should be
# solution(cell) = 2.



# For cell = "c2", the output should be
# solution(cell) = 6.



def solution(cell):
    x, y = ord(cell[0]) - ord('a') + 1, int(cell[1])
    possible_moves = [
        (x + 2, y + 1), (x + 2, y - 1),
        (x - 2, y + 1), (x - 2, y - 1),
        (x + 1, y + 2), (x - 1, y + 2),
        (x + 1, y - 2), (x - 1, y - 2)
    ]

    valid_moves = sum(1 for move in possible_moves if 1 <= move[0] <= 8 and 1 <= move[1] <= 8)
    return valid_moves


# Pawn race is a game for two people, played on an ordinary 8 × 8 chessboard. The first player has a white pawn, the second one - a black pawn. Initially the pawns are placed somewhere on the board so that the 1st and the 8th rows are not occupied. Players take turns to make a move.

# White pawn moves upwards, black one moves downwards. The following moves are allowed:

# one-cell move on the same vertical in the allowed direction;
# two-cell move on the same vertical in the allowed direction, if the pawn is standing on the 2nd (for the white pawn) or the 7th (for the black pawn) row. Note that even with the two-cell move a pawn can't jump over the opponent's pawn;
# capture move one cell forward in the allowed direction and one cell to the left or to the right.


# The purpose of the game is to reach the the 1st row (for the black pawn) or the 8th row (for the white one), or to capture the opponent's pawn.

# Given the initial positions and whose turn it is, determine who will win or declare it a draw (i.e. it is impossible for any player to win). Assume that the players play optimally.

# Example

# For white = "e2", black = "e7", and toMove = 'w', the output should be
# solution(white, black, toMove) = "draw";
# For white = "e3", black = "d7", and toMove = 'b', the output should be
# solution(white, black, toMove) = "black";
# For white = "a7", black = "h2", and toMove = 'w', the output should be
# solution(white, black, toMove) = "white".

def solution(white, black, to_move):
    white_position = int(white[1])
    black_position = int(black[1])
    if white[0] == black[0] and white_position < black_position:
        return "draw"

    equal_position = {2: 7, 3: 6, 4: 5, 5: 4, 6: 3, 7: 2}
    can_capture = abs(ord(white[0]) - ord(black[0])) == 1

    if can_capture:
        if white_position + 1 == black_position:
            return "white" if to_move == "w" else "black"
        if white_position == 2 and black_position == 7:
            return "black" if to_move == "w" else "white"

        if white_position == 2:
            if to_move == "b":
                black_position -= 1
            if white_position + 1 == black_position:
                return "white"
            winner1 = mock_game(white_position + 1, black_position, to_move)
            winner2 = mock_game(white_position + 2, black_position, to_move)
            if winner1 == "white" or winner2 == "white":
                return "white"
            return "black"

        if black_position == 7:
            if to_move == "w":
                white_position += 1
            if white_position + 1 == black_position:
                return "black"
            winner1 = mock_game(white_position, black_position - 1, to_move)
            winner2 = mock_game(white_position, black_position - 2, to_move)
            if winner1 == "black" or winner2 == "black":
                return "black"
            return "white"

        return mock_game(white_position, black_position, to_move)
    else:
        black_position = equal_position[black_position]
        white_position += 2 if white_position == 2 else 1
        black_position += 2 if black_position == 2 else 1

        if white_position == black_position:
            return "white" if to_move == "w" else "black"

        return "white" if white_position > black_position else "black"


def mock_game(white_position, black_position, to_move):
    while white_position != 8 and black_position != 1:
        white_position += 1 if to_move == "w" else 0
        black_position -= 1 if to_move == "b" else 0
        if white_position + 1 == black_position:
            return "black" if to_move == "w" else "white"

        if white_position == 8:
            return "white"
        if black_position == 1:
            return "black"

        black_position -= 1 if to_move == "w" else 0
        white_position += 1 if to_move == "b" else 0
        if white_position + 1 == black_position:
            return "white" if to_move == "w" else "black"

    return "white" if white_position == 8 else "black"

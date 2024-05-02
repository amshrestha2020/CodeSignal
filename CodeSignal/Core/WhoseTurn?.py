# Imagine a standard chess board with only two white and two black knights placed in their standard starting positions: the white knights on b1 and g1; the black knights on b8 and g8.



# There are two players: one plays for white, the other for black. During each move, the player picks one of his knights and moves it to an unoccupied square according to standard chess rules. Thus, a knight on d5 can move to any of the following squares: b6, c7, e7, f6, f4, e3, c3, and b4, as long as it is not occupied by either a friendly or an enemy knight.



# The players take turns in making moves, starting with the white player. Given the configuration p of the knights after an unspecified number of moves, determine whose turn it is.

# Example

# For p = "b1;g1;b8;g8", the output should be
# solution(p) = true.

# The configuration corresponds to the initial state of the game. Thus, it's white's turn.



def solution(p):
    white_point = 0
    black_point = 0

    positions = p.split(";")
    is_starting_white = {
        'a': False,
        'b': True,
        'c': False,
        'd': True,
        'e': False,
        'f': True,
        'g': False,
        'h': True,
    }

    if check_is_white(positions[0], is_starting_white):
        white_point += 1
    if check_is_white(positions[1], is_starting_white):
        white_point += 1
    if check_is_white(positions[2], is_starting_white):
        black_point += 1
    if check_is_white(positions[3], is_starting_white):
        black_point += 1

    if white_point == black_point:
        return True
    if abs(white_point - black_point) == 2:
        return True
    return False

def check_is_white(location, is_starting_white):
    letter = location[0]
    number = int(location[1])

    if is_starting_white[letter]:
        return number % 2 == 1
    return number % 2 == 0

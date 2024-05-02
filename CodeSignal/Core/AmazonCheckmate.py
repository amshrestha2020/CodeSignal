# An amazon (also known as a queen + knight compound) is an imaginary chess piece that can move like a queen or a knight (or, equivalently, like a rook, bishop, or knight). The diagram below shows all squares which the amazon can attack from e4 (circles represent knight-like moves while crosses correspond to queen-like moves).



# Recently, you've come across a diagram with only three pieces left on the board: a white amazon, the white king, and the black king. It's black's move. You don't have time to determine whether the game is over or not, but you'd like to figure it out in your head. Unfortunately, the diagram is smudged and you can't see the position of the black king, so you'll need to consider all possible positions.

# Given the positions of the white pieces on a standard chessboard (using algebraic notation), your task is to determine the number of possible black king's positions such that:

# it's checkmate (i.e. black's king is under the amazon's attack and it cannot make a valid move);
# it's check (i.e. black's king is under the amazon's attack but it can reach a safe square in one move);
# it's stalemate (i.e. black's king is on a safe square but it cannot make a valid move);
# black's king is on a safe square and it can make a valid move.
# Note that two kings cannot be placed on two adjacent squares (including two diagonally adjacent ones).

# Example

# For king = "d3" and amazon = "e4", the output should be
# solution(king, amazon) = [5, 21, 0, 29].



# Red crosses correspond to the checkmate positions, orange pluses refer to check positions, and green circles denote safe squares.

# For king = "a1" and amazon = "g5", the output should be
# solution(king, amazon) = [0, 29, 1, 29].



# The stalemate position is marked by a blue square.

def solution(king, amazon):
    def x(position):
        return ord(position[0]) - ord('a') + 1

    def y(position):
        return int(position[1])

    kx, ky, ax, ay = x(king), y(king), x(amazon), y(amazon)
    a = [0, 0, 0, 0]

    for i in range(1, 9):
        for j in range(1, 9):
            if not one_away(kx, ky, i, j) and not (ax == i and ay == j):
                threatened = is_threatened(i, j, kx, ky, ax, ay)
                mate = not one_away(ax, ay, i, j) or one_away(ax, ay, kx, ky)

                if mate:
                    for k in range(i - 1, i + 2):
                        for l in range(j - 1, j + 2):
                            if space_open(i, j, k, l, kx, ky) and not is_threatened(k, l, kx, ky, ax, ay):
                                mate = False
                                break

                if threatened:
                    a[0] += mate
                    a[1] += not mate
                else:
                    a[2] += mate
                    a[3] += not mate

    return a

def is_threatened(x, y, kx, ky, ax, ay):
    return (
        (ax == x and not (kx == ax and (ky - ay) * (ky - y) < 0)) or
        (ay == y and not (ky == ay and (kx - ax) * (kx - x) < 0)) or
        (abs(ax - x) == abs(ay - y) and not (abs(kx - x) == abs(ky - y) and (kx - ax) * (kx - x) < 0)) or
        (ax != x and ay != y and abs(ax - x) + abs(ay - y) == 3)
    )

def one_away(x1, y1, x2, y2):
    return abs(x2 - x1) <= 1 and abs(y2 - y1) <= 1

def space_open(i, j, x, y, kx, ky):
    return (
        not (x == i and y == j) and
        1 <= x <= 8 and
        1 <= y <= 8 and
        not one_away(x, y, kx, ky)
    )


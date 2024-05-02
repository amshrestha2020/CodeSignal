# Let's play Tetris! But first we need to define the rules, especially since they probably differ from the way you've played Tetris before.

# There is an empty field with 20 rows and 10 columns, which is initially empty. Random pieces appear on the field, each composed of four square blocks. You can't change the piece's shape, but you can rotate it 90 degree clockwise (possibly several times) and choose which columns it will appear within. Once you've rotated the piece and have set its starting position, it appears at the topmost row where you placed it and falls down until it can't fall any further. The objective of the game is to create horizontal lines composed of 10 blocks. When such a line is created, it disappears, and all lines above the deleted one move down. The player receives 1 point for each deleted row.

# Your task is to implement an algorithm that places each new piece optimally. The piece is considered to be placed optimally if:

# The total number of blocks in the rows this piece will occupy after falling down is maximized;
# Among all positions with that value maximized, this position requires the least number of rotations;
# Among all positions that require the minimum number of rotations, this one is the leftmost one (i.e. the leftmost block's position is as far to the left as possible).
# The piece can't leave the field. It is guaranteed that it is always possible to place the Tetris piece in the field.

# Implement this algorithm and calculate the number of points that you will get for the given set of pieces.

# Example

# For

# pieces = [[[".", "#", "."], 
#            ["#", "#", "#"]],
#           [["#", ".", "."], 
#            ["#", "#", "#"]],
#           [["#", "#", "."], 
#            [".", "#", "#"]],
#           [["#", "#", "#", "#"]],
#           [["#", "#", "#", "#"]],
#           [["#", "#"], 
#            ["#", "#"]]]
# the output should be
# solution(pieces) = 1.

# For this explanation, we are representing each block by the index of the piece it belongs to. After the first 5 blocks fall, the field looks like this:

# ...
# . . . . . . . . . .
# . . . . . . . . . .
# . . . . . . . . . .
# . . . . . . . . . .
# . . . . . . . . 3 4
# . . . . . . . . 3 4
# . 0 . 1 . 2 2 . 3 4
# 0 0 0 1 1 1 2 2 3 4

# Note that the 0th, 1st, and 2nd pieces all fell down without rotating, while the 3rd and the 4th pieces were rotated one time each.

# Since there is now a row composed of 10 blocks, it is deleted, and you get 1 point.

# When the last piece falls, the final field looks like this:

# ...
# . . . . . . . . . .
# . . . . . . . . . .
# . . . . . . . . . .
# . . . . . . . . . .
# . . . . . . . . . .
# 5 5 . . . . . . 3 4
# 5 5 . . . . . . 3 4
# . 0 . 1 . 2 2 . 3 4



def solution(pieces):
    res = 0
    board = [['.' for _ in range(10)] for __ in range(20)]
    for p in pieces:
        choice = find_the_best_choice(board, p)
        for _ in range(choice[1]):
            p = rotate_piece(p)
        fix_the_piece(board, p, choice[3], choice[2])
        filled = get_full_lines(board)
        for i in filled:
            clear_the_filled_line(board, i)
            res += 1
    return res

def rotate_piece(p):
    return list(map(list, zip(*reversed(p))))

def throw_piece(board, piece, col):
    episode = [row[:] for row in board]
    pi = len(piece)
    pj = len(piece[0])
    row = 0
    is_fixed = True
    while is_fixed:
        is_fixed = True
        for i in range(pi):
            for j in range(pj):
                if board[row + i][col + j] == '#' and piece[i][j] == '#':
                    is_fixed = False
                    break
            if not is_fixed:
                break
        if is_fixed:
            row += 1
        if row == len(board) - pi + 1:
            break
    row -= 1
    return row

def get_full_lines(board):
    return [i for i, row in enumerate(board) if '.' not in row]

def clear_the_filled_line(board, i):
    del board[i]
    board.insert(0, ['.' for _ in range(10)])

def fix_the_piece(board, piece, row, col):
    pi = len(piece)
    pj = len(piece[0])
    for i in range(pi):
        for j in range(pj):
            board[row + i][col + j] = '#' if piece[i][j] == '#' else board[row + i][col + j]

def find_the_best_choice(board, piece):
    choices = []
    p = [row[:] for row in piece]
    for r in range(4):
        if r > 0:
            p = rotate_piece(p)
        for col in range(len(board[0]) - len(p[0]) + 1):
            row = throw_piece(board, p, col)
            blocks = sum(row.count('#') for row in board[row:row + len(p)])
            choices.append((blocks, r, col, row))
    return max(choices, key=lambda x: (x[0], -x[1], -x[2]))

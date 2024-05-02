# John has always had trouble remembering chess game positions. To help himself with remembering, he decided to store game positions in strings. He came up with the following position notation:

# The notation is built for the current game position row by row from top to bottom, with '/' separating each row notation;
# Within each row, the contents of each square are described from the leftmost column to the rightmost;
# Each piece is identified by a single letter taken from the standard English names ('P' = pawn, 'N' = knight, 'B' = bishop, 'R' = rook, 'Q' = queen, 'K' = king);
# White pieces are designated using upper-case letters ("PNBRQK") while black pieces use lowercase ("pnbrqk");
# Empty squares are noted using digits 1 through 8 (the number of empty squares from the last piece);
# Empty lines are noted as "8".
# For example, for the initial position (shown in the picture below) the notation will look like this:

# "rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR"



# After the white pawn moves from e2 to e4, the notation will be as follows:

# "rnbqkbnr/pppppppp/8/8/4P3/8/PPPP1PPP/RNBQKBNR"

# John has written down some positions using his notation, and now he wants to rotate the board 90 degrees clockwise and see what notation for the new board would look like. Help him with this task.

# Example

# For notation = "rnbqkbnr/pppppppp/8/8/4P3/8/PPPP1PPP/RNBQKBNR", the output should be
# solution(notation) = "RP4pr/NP4pn/BP4pb/QP4pq/K2P2pk/BP4pb/NP4pn/RP4pr".

# The notation corresponds to the initial position with one move made (white pawn from e2 to e4).
# After rotating the board, it will look like this:



# So, the notation of the new position is "RP4pr/NP4pn/BP4pb/QP4pq/K2P2pk/BP4pb/NP4pn/RP4pr".



import itertools

def solution(notation):
    # Split the notation into rows
    rows = notation.split('/')
    # Expand the rows to account for empty squares
    expanded_rows = [''.join('8' * int(c) if c.isdigit() else c for c in row) for row in rows]
    # Initialize an empty list for the rotated rows
    rotated_rows = []
    # Iterate over the columns from left to right
    for i in range(8):
        # Initialize an empty string for the rotated row
        rotated_row = ''
        # Iterate over the rows from bottom to top
        for row in expanded_rows[::-1]:
            # Add the piece or empty square
            rotated_row += row[i]
        # Compress the rotated row to use digits for empty squares
        compressed_row = ''.join(str(len(list(g))) if k == '8' else ''.join(g) for k, g in itertools.groupby(rotated_row))
        # Add the compressed row to the list of rotated rows
        rotated_rows.append(compressed_row)
    # Join the rotated rows with '/' and return the result
    return '/'.join(rotated_rows)


# Test case
notation = "rnbqkbnr/pppppppp/8/8/4P3/8/PPPP1PPP/RNBQKBNR"
print(solution(notation))  # Output: "RP4pr/NP4pn/BP4pb/QP4pq/K2P2pk/BP4pb/NP4pn/RP4pr"

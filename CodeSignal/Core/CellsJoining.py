# You are writing a spreadsheet application for an ancient operating system. The system runs on a computer so old that it can only display ASCII graphics. Currently you are stuck with implementing the cells joining algorithm.

# You are given a table in ASCII graphics, where the following characters are used for borders: +, -, |. The rows can have different heights and the columns can have different widths. Each cell has an area greater than 1 (excluding the borders) and can contain any ASCII characters excluding +, - and |.

# The algorithm you want to implement should merge the cells within a given rectangular part of the table into a single cell by removing the borders between them (i.e. replace them with space characters (' ') and replace redundant +s with correct border symbols). The cells to join are represented by the coordinates of the cells at the extreme bottom-left and top-right of the area.

# Example
# For

# table = ["+----+--+-----+----+",
#          "|abcd|56|!@#$%|qwer|",
#          "|1234|78|^&=()|tyui|",
#          "+----+--+-----+----+",
#          "|zxcv|90|77777|stop|",
#          "+----+--+-----+----+",
#          "|asdf|~~|ghjkl|100$|",
#          "+----+--+-----+----+"]
# and coords = [[2, 0], [1, 1]], the output should be

# solution(table, coords) = ["+----+--+-----+----+",
#                            "|abcd|56|!@#$%|qwer|",
#                            "|1234|78|^&=()|tyui|",
#                            "+----+--+-----+----+",
#                            "|zxcv 90|77777|stop|",
#                            "|       +-----+----+",
#                            "|asdf ~~|ghjkl|100$|",
#                            "+-------+-----+----+"]


import numpy as np
import re

def solution(table, coords):
    # Convert the table to a numpy array for easier manipulation
    table = np.array([list(i) for i in table])

    # Find the indices of the column and row borders
    col = [i for i, j in enumerate(table[0]) if j == '+']
    row = [i for i, j in enumerate(table) if j[0] == '+']

    # Ensure the coordinates are within the bounds of the table
    if not (0 <= coords[0][0] < len(row) and 0 <= coords[1][0] < len(row) and
            0 <= coords[0][1] < len(col) and 0 <= coords[1][1] < len(col)):
        return "Invalid coordinates"

    # Get the rows and columns to be modified
    m, n, x, y = coords[1] + coords[0]
    g, h , p , q, k = col[y] + 1, col[n + 1], row[m] + 1, row[x + 1], len(table)

    # Remove the internal borders within the specified rectangle
    for i in row[m + 1: x + 1]:
        table[i, g: h] = ' '
    for i in col[y + 1: n + 1]:
        table[p: q, i] = ' '

    # Replace the outer borders with '|' or '-' if they are on the edge of the table
    if m == 0:
        table[0, g: h] = '-'
    if row[x + 1] == k - 1:
        table[-1, col[y] + 1: col[n + 1 ]] = '-'
    if y == 0:
        table[p: q, 0] = '|'
    if col[n + 1] == len(table[0]) - 1:
        table[p: q, -1] = '|'

    # Convert the table back to a list of strings
    return [''.join(x) for x in table]

# Not long ago you saw an orienteering competition on TV and immediately wanted to try it yourself. You've joined an orienteering club and started preparing for the upcoming competitions.

# You've just came home from one particularly exhausting competition and decided to relax by playing a board game which all qualified participants (including you, of course) got as a reward. In this game your objective is to navigate your way on the board from the start located in the upper-left corner to the finish located in the bottom-right corner in as little time as possible.

# The game board is a rectangle divided into equal cells. Each cell contains a number denoting the time you should wait in this cell before advancing to the next one. From each cell you can move only to the neighboring one, i.e. the one directly below, above, to the left or to the right of your current position.

# Given the game board find the minimum time required to reach the finish from the start.

# Example

# For

# board = [[42, 51, 22, 10,  0 ],
#          [2,  50, 7,  6,   15],
#          [4,  36, 8,  30,  20],
#          [0,  40, 10, 100, 1 ]]
# the output should be
# solution(board) = 140.

# Example

import heapq

def solution(board):
    q = [(board[0][0], 0, 0)]  # (distance, x, y)
    visited = {(0, 0)}
    while q:
        weight, x, y = heapq.heappop(q)
        for dx, dy in [(0, 1), (0, -1), (-1, 0), (1, 0)]:
            nx, ny = x + dx, y + dy
            if 0 <= nx < len(board) and 0 <= ny < len(board[0]) and (nx, ny) not in visited:
                if (nx, ny) == (len(board) - 1, len(board[0]) - 1):
                    return weight
                visited.add((nx, ny))
                heapq.heappush(q, (weight + board[nx][ny], nx, ny))
    return 0

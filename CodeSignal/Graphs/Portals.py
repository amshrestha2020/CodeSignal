# Little Ratiorg was so tired of being bullied by other bots and mighty CodeFighters that he decided to join the Ninja Bots Training camp. It is known that any bot that manages to solve all the challenges becomes an ultimate master of algorithms, and that is exactly what Ratiorg is aiming at.

# Ratiorg has already improved his physical strength considerably, and now it's time to hone his mental skills. As it turned out, the bot has what it takes to be a great magician: he has what appears to be an infinite source of mana somewhere inside his little mechanical body. In the next challenge, Ratiorg will have to use it. The bot is standing in the top left corner of the rectangular grid, some cells of which are impassable. His goal is to make it to the bottom right corner in no more than maxTime seconds.

# Ratiorg can move between two passable cells if they share a common side, and each move takes 1 second. He can also set an arbitrary number of portals into passable cells; moreover, he can even set them remotely and instantly, i.e. there's no need to reach the cell to set a portal there, and setting a portal takes no time. Ratiorg can instantly move between any pair of cells with portals. However, setting a portal to the cell at (x, y) costs manacost[x][y] mana points.

# Given the maxTime and the manacost matrix, calculate the minimum amount of mana Ratiorg will have to use to finish the challenge in time.

# Example

# For maxTime = 4 and

# manacost = [[1, -1, -1],
#             [5, -1, -1],
#             [4,  6,  8]]
# the output should be solution(maxTime, manacost) = 0.

# The cheapest way to get to the bottom right corner takes 4 seconds and doesn't require any portals.

# For maxTime = 3 and

# manacost = [[1, -1, -1],
#             [5, -1, -1],
#             [4,  6,  8]]
# the output should be
# solution(maxTime, manacost) = 5.

# The best plan is to set portals into the top left and the bottom left corners (the total manacost equals 1 + 4 = 5). After that, you can reach the bottom left corner instantly and then make two moves rightwards in 2 seconds.


import numpy as np
from collections import defaultdict

def solution(maxTime, manacost):
    row, col = len(manacost), len(manacost[0])

    def dfs(x, y, head=True):
        dp = defaultdict(set)
        seen = np.array(manacost)
        queue = [(x, y, 0)]
        seen[x, y] = 1
        while queue:
            x, y, dis = queue.pop(0)
            if dis <= maxTime:
                if head and x == row - 1 and y == col - 1:
                    return 1
                dp[dis].add(manacost[x][y])
                for dx, dy in [(0, 1), (1, 0), (-1, 0), (0, -1)]:
                    nx, ny = x + dx, y + dy
                    if 0 <= nx < row and 0 <= ny < col and seen[nx, ny] != -1:
                        seen[nx, ny] = -1
                        queue.append((nx, ny, dis + 1))
        return {x: min(y) for x, y in dp.items()}

    start = dfs(0, 0)
    if start == 1:
        return 0

    min_mana = float('inf')
    end = dfs(row - 1, col - 1, False)
    for step, mana in start.items():
        leftTime = maxTime - step
        min_mana = min(min_mana, min(y for x, y in end.items() if x <= leftTime) + mana)

    return min_mana

# You decide to send your troops to the Logging Camp to gather some lumber. Like any good Commander, you first need to make sure that your enemy's troops (which are heading to the same Logging Camp) won't get there first.

# The world map can be represented as an infinite grid of hexagonal cells (a Hex Map). Each cell is uniquely defined by its coordinates as shown below:



# Your troops, your enemy's troops and the Logging Camp each occupies exactly one cell.

# There are 2 types of cells, those that are passable and those that are impassable. Troops can move from one passable cell to another if they share a common side. Such a move takes k seconds where k represents the size of the troops.

# Both you and your enemy are so eager to get to the Logging Camp that you ignore each other's troop movements. In other words, you can both safely occupy the same cell at the same time (including the initial cell).

# Given the locations of the troops and the Logging Camp, find out if your troops can reach their destination earlier than your enemy.

# Example

# For friendlyTroops = [-2, 2, 3], enemyTroops = [1, 0, 9], loggingCamp = [0, 0], and impassableCells = [[-1, 1]], the output should be
# solution(friendlyTroops, enemyTroops, loggingCamp, impassableCells) = false.

# Your troops need 3 * 3 = 9 seconds to reach the Logging Camp (one of the optimal paths is (-2, 2) -> (-2, 1) -> (-1, 0) -> (0, 0), i.e. 3 marches taking 3 seconds each). Your enemy's troops will arrive in 9 * 1 = 9 (1 march taking 9 seconds) seconds as well.



# For friendlyTroops = [-2, 2, 3], enemyTroops = [1, 0, 9], loggingCamp = [0, 0], and impassableCells = [], the output should be
# solution(friendlyTroops, enemyTroops, loggingCamp, impassableCells) = true.

# Your troops need 3 * 2 = 6 seconds to reach the Logging Camp (the optimal paths is (-2, 2) -> (-1, 1) -> (0, 0), i.e. 2 marches taking 3 seconds each). Your enemy's troops will arrive in only 9 seconds


from collections import deque
from heapq import heappop, heappush

def solution(friendlyTroops, enemyTroops, loggingCamp, impassableCells):
    impassableCells = set(tuple(cell) for cell in impassableCells)
    directions = [(1, 0), (-1, 0), (0, 1), (0, -1), (-1, 1), (1, -1)]
    
    def bfs(start, speed):
        queue = [(0, start)]
        visited = set()
        while queue:
            time, cell = heappop(queue)
            if cell in visited:
                continue
            visited.add(cell)
            if cell == tuple(loggingCamp):
                return time
            for dx, dy in directions:
                x, y = cell[0] + dx, cell[1] + dy
                if (x, y) not in visited and (x, y) not in impassableCells:
                    heappush(queue, (time + speed, (x, y)))
        return float('inf')
    
    friendlyTime = bfs(tuple(friendlyTroops[:2]), friendlyTroops[2])
    enemyTime = bfs(tuple(enemyTroops[:2]), enemyTroops[2])
    
    return friendlyTime < enemyTime

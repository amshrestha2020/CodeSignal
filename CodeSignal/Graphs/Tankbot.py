# Little Ratiorg was so tired of being bullied by other bots and mighty CodeFighters that he decided to join the Ninja Bots Training camp. It is known that any bot that manages to solve all the challenges becomes an ultimate master of algorithms, and that is exactly what Ratiorg is aiming at.

# His training is now officially over, and Ratiorg is ready to get back to CodeSignal and show who's the boss. To make his appearance more imposing, Ratiorg is planning to take a tank and drive it back home. However, the bot will have to travel through the forest covered in trees so strong that they can hold back even a tank, so not every tank can make it through this forest.

# Since Ratiorg finished the trainings as the best student, he can pick any tank he likes. There are a lot of tanks of all possible sizes. All available tanks are square, can only move in one of the four directions (leftwards, rightwards, downwards or upwards), and can't move over the trees.

# The Ninja Bots Training camp is located at the top left corner of the forest, and CodeFigts bots camp is located at its bottom right corner. Given the map of the forest, find the maximum size of the tank Ratiorg can take in order to get from the training camp to the CodeFigths bot camp.

# Example

# For

# forest =  [[true, true, true,  true],
#            [true, true, false, true],
#            [true, true, true,  true],
#            [true, true, true,  true]]
# the output should be
# solution(forest) = 2.



# For

# forest = [[false, true, true],
#           [true,  true, true]]
# the output should be
# solution(forest) = 0.

# There is a tree right at the entrance of the Training Camp, so there's no way to get out of there by tank.


import numpy as np

def solution(forest):
    row, col, max_size = len(forest), len(forest[0]), 0

    def valid(x1, y1, x2, y2, size, passed):
        f = passed[x1:x2, y1:y2].flatten()
        return all(f) and any(f == 1) and 0 <= x1 <= row - size and 0 <= y1 <= col - size

    def bfs(size):
        queue = [(0, 0, size, size)]
        passed = np.array(forest, dtype=int)
        if not valid(0, 0, size, size, size, passed):
            return 0
        passed[0:size, 0:size] = -1
        while queue:
            x1, y1, x2, y2 = queue.pop(0)
            if x1 == row - size and y1 == col - size:
                return 1
            for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                nx1, ny1, nx2, ny2 = x1 + dx, y1 + dy, x2 + dx, y2 + dy
                if valid(nx1, ny1, nx2, ny2, size, passed):
                    passed[nx1:nx2, ny1:ny2] = -1
                    queue.append((nx1, ny1, nx2, ny2))
        return 0

    while bfs(max_size + 1):
        max_size += 1

    return max_size

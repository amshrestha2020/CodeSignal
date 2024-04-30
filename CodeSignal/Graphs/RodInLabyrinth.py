# After long years of sharpening your programming skills and honing your physique you finally made it: as a member of the ProProgrammers team you've entered Fort Boyard!

# Your team has successfully completed several challenges so far, and one of your teammates is ready to face the next one. In this challenge the participant finds himself in a rectangular labyrinth, and his goal is to carry the rod from the top left corner of the labyrinth to the bottom right corner. This rod is not exactly the lightest thing you can imagine, so the participant would naturally want do it as fast as possible.

# You decided to determine in advance if it's possible to complete this challenge, and if it is, find the minimal number of moves required to carry the rod through the labyrinth. The labyrinth can be represented as a rectangular matrix some cells of which are marked as blocked, and the rod can be represented as a 1 × 3 rectangle. The rod can't collide with the blocked cells or the walls, so it's impossible to move it into position in which one of its cells coincides with the blocked cell or the wall. The goal is thus to move the rod into position in which one of its cells is in the bottom right cell of the labyrinth.

# There are 5 types of moves that the participant can perform: move the rod one cell down or up, to the right or to the left, or to change its orientation from vertical to horizontal and vice versa. The rod can only be rotated about its center, and only if the 3 × 3 area surrounding it is clear from the obstacles or the walls.

# The rod is initially positioned horizontally, and its left cell lies in [0, 0].

# Example

# For

# labyrinth = [['.', '.', '.', '.', '.', '.', '.', '.', '.'],
#              ['#', '.', '.', '.', '#', '.', '.', '.', '.'],
#              ['.', '.', '.', '.', '#', '.', '.', '.', '.'],
#              ['.', '#', '.', '.', '.', '.', '.', '#', '.'],
#              ['.', '#', '.', '.', '.', '.', '.', '#', '.']]
# the output should be
# solution(labyrinth) = 11.

# You can see one of the possible optimal paths in the image below:


# For

# labyrinth = [['.', '.', '.', '.', '.', '.', '.', '.', '.'],
#              ['#', '.', '.', '.', '#', '.', '.', '#', '.'],
#              ['.', '.', '.', '.', '#', '.', '.', '.', '.'],
#              ['.', '#', '.', '.', '.', '.', '.', '#', '.'],
#              ['.', '#', '.', '.', '.', '.', '.', '#', '.']]
# the output should be
# solution(labyrinth) = -1.

# This example is similar to the previos one except one '#', so you can check it on the image above.


from collections import deque

def solution(labyrinth):
    h, w = len(labyrinth), len(labyrinth[0])
    visited = [[[False]*w for _ in range(h)] for _ in range(2)]

    class Triple:
        def __init__(self, first, second, third, move):
            self.first = first
            self.second = second
            self.third = third
            self.move = move

        def __getitem__(self, i):
            if i == 0:
                return self.first
            elif i == 1:
                return self.second
            else:
                return self.third

    q = deque()
    q.append(Triple(0, 0, 0, 0))

    while q:
        cur = q.popleft()
        x, y = cur[0], cur[1]
        if cur[2] == 0:
            if x < 0 or x + 2 >= w or y < 0 or y >= h:
                continue
            if labyrinth[y][x] == '#' or labyrinth[y][x + 1] == '#' or labyrinth[y][x + 2] == '#':
                continue
            if x + 2 == w - 1 and y == h - 1:
                return cur.move
            if visited[0][y][x]:
                continue
            free = True
            for i in range(x, x + 3):
                for j in range(y - 1, y + 2):
                    if j < 0 or j >= h or labyrinth[j][i] == '#':
                        free = False
            if free:
                q.append(Triple(x + 1, y - 1, 1, cur.move + 1))
        else:
            if x < 0 or x >= w or y < 0 or y + 2 >= h:
                continue
            if labyrinth[y][x] == '#' or labyrinth[y + 1][x] == '#' or labyrinth[y + 2][x] == '#':
                continue
            if x == w - 1 and y + 2 == h - 1:
                return cur.move
            if visited[1][y][x]:
                continue
            free = True
            for i in range(x - 1, x + 2):
                for j in range(y, y + 3):
                    if i < 0 or i >= w or labyrinth[j][i] == '#':
                        free = False
            if free:
                q.append(Triple(x - 1, y + 1, 0, cur.move + 1))
        visited[cur[2]][y][x] = True
        q.append(Triple(x - 1, y, cur[2], cur.move + 1))
        q.append(Triple(x + 1, y, cur[2], cur.move + 1))
        q.append(Triple(x, y - 1, cur[2], cur.move + 1))
        q.append(Triple(x, y + 1, cur[2], cur.move + 1))

    return -1

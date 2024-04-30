# Little Ratiorg was tired of being bullied by other bots and mighty CodeFighters, so he joined the Ninja Bots Training camp. Any bot that manages to solve all the challenges becomes an ultimate master of algorithms, and that is exactly what Ratiorg wants.

# It's been several weeks, and Ratiorg is getting strong enough that he's making some enemies. They're starting to feel threatened, which is why they sabotaged his next challenge. Here's how they did it:

# Ratiorg is about to be locked up in one of multiple rooms in a rectangular hangar. The rooms are securely locked: it is possible to leave a room only in one direction specific to this room. The problem is, the villains have messed the system up, so now there is no way to finish the challenge from certain rooms. The challenge will be over if Ratiorg successfully leaves the hangar (i.e. leaves the rectangle that represents it).

# To figure out the odds of Ratiorg's success, you'd like to calculate the number of rooms, starting from which Ratiorg won't be able to finish the challenge. Implement a function that will return this number.

# Example

# For

# hangar = [['U', 'L'],
#           ['R', 'L']]
# the output should be
# solution(hangar) = 2.

# Ratiorg won't be able to get out of the hangar if he starts from either of the bottom rooms.

# Check out the image below for more context:

def solution(hangar):
    n, m = len(hangar), len(hangar[0])
    dx = {'U': -1, 'D': 1, 'L': 0, 'R': 0}
    dy = {'U': 0, 'D': 0, 'L': -1, 'R': 1}
    visited = [[False]*m for _ in range(n)]
    can_leave = [[False]*m for _ in range(n)]

    def dfs(x, y):
        if not (0 <= x < n and 0 <= y < m):
            return True
        if visited[x][y]:
            return can_leave[x][y]
        visited[x][y] = True
        nx, ny = x + dx[hangar[x][y]], y + dy[hangar[x][y]]
        can_leave[x][y] = dfs(nx, ny)
        return can_leave[x][y]

    return sum(not dfs(i, j) for i in range(n) for j in range(m))

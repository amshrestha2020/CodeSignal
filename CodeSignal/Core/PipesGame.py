# Carlos always loved playing video games, especially the well-known computer game "Pipes". Today he finally decided to write his own version of the legendary game from scratch.

# In this game the player has to place the pipes on a rectangular field to make water pour from each source to a respective sink. He has already come up with the entire program, but one question still bugs him: how can he best check that the arrangement of pipes is correct?

# It's your job to help him figure out exactly that.

# Carlos has 7 types of pipes in his game, with numbers corresponding to each type:

# 1 - vertical pipe
# 2 - horizontal pipe
# 3-6 - corner pipes
# 7 - two pipes crossed in the same cell (note that these pipes are not connected)
# Here they are, pipes 1 to 7, respectively:



# Water pours from each source in each direction that has a pipe connected to it (thus it can even pour in all four directions). The puzzle is solved correctly only if all water poured from each source eventually reaches a corresponding sink.

# Help Carlos check whether the arrangement of pipes is correct. If it is correct, return the number of cells with pipes that will be full of water at the end of the game. If not, return -X, where X is the number of cells with water before the first leakage point is reached, or if the first drop of water reaches an incorrect destination (whichever comes first). Assume that water moves from one cell to another at the same speed.

# Example

# For

# state = ["a224C22300000",
#          "0001643722B00",
#          "0b27275100000",
#          "00c7256500000",
#          "0006A45000000"]
# the output should be solution(state) = 19.

# Here is how the game will end:

import numpy

def solution(state):
    fail = []
    row, col = len(state), len(state[0])
    times = numpy.full((row,col), float('inf'))
    target = set()
    d = {'1':[(1,0),(-1,0)],'2':[(0,1),(0,-1)],'3':[(0,1),(1,0)],'4':[(0,-1),(1,0)],\
        '5':[(0,-1),(-1,0)],'6':[(0,1),(-1,0)],'7':[(0,1),(0,-1),(1,0),(-1,0),]}
    state = numpy.array(state)
    def valid(x,y,symbol = None):
        return  0<=x<row and 0<= y <col and ('1' <= state[x][y] <= '9' or symbol and symbol.upper() == state[x][y])
          
    def find(x, y, symbol):
        d[symbol] = []
        for i,j in (0,1),(1,0),(-1,0),(0,-1):
            if valid(x+i,y+j):
                for m,n in d[state[x+i][y+j]]:
                    if m + i == 0 and n+j == 0:
                        d[symbol].append((i,j)) 
    def dfs(m, x, y, symbol, time):
        queue = [(m, x, y, time)]
        while queue:
            m, x, y, time = queue.pop(0)
            times[x,y] = min(times[x,y],time)
            f = 0
            if state[x][y] == symbol.upper():
                target.add((x,y))
                continue
            if state[x][y] == '7':
                direction = [(0,1),(0,-1)] if m == 0 else [(1,0),(-1,0)]
            else:
                direction = d[state[x][y]]
            for i,j in direction :
                if valid(x+i,y+j,symbol) and not visited[x+i][y+j]:
                    f = 1
                    visited[x+i,y+j] = 1 if state[x+i][y+j] != symbol.upper() else 0
                    queue.append((i, x+i, y+j, time+1))
            if not f:
                fail.append([x,y])
                return 0
        return 1
    
    count = 0
    check = []
    for i in range(row):
        for j in range(col):
            if 'a' <= state[i][j] <= 'z':
                count += 1
                visited = numpy.zeros((row, col))
                find(i, j, state[i][j])
                if d.get(state[i][j], 0):
                    k = dfs(-1, i, j, state[i][j], 0)
                    check.append(k)  
                else:
                    check.append(0)
                    times[i][j] = 0
    for x,y in target:
        times[x, y] = float('inf')
    if all(check):
        return len(times[times < float('inf')]) - count
    else:
        if not fail:
            return len(times[times < float('inf')]) - count
        max_time = min(times[x,y] for x,y in fail) 
        return -len(times[times <= max_time]) + count

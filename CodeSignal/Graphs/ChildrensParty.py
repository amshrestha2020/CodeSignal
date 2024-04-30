# You are the leader of a tribe living on a remote island covered by a rectangular grid. Your tribe consists of several families, with a single child in each family. Each cell is occupied by exactly one family. Today is a special day: a children's party is organized! The ultimate game was prepared to keep the children entertained. At the very beginning of the game, all children of the island have to form several teams. Members of the same team should be able to communicate with each other, so every child of a team should be able to reach every other child of this team. A child can move from one cell to another if these two cells are adjacent (they have a common side). Children are strictly prohibited to go beyond the island.

# Because of the wild animals living on your island, it is not always safe to move from a cell to one of the adjacent ones: hungry beasts are watching the paths between them closely, hoping to spot a child and attack them. For each cell you know the paths the animals are watching, with respect to this cell. The children are also aware of the dangerous paths and won't take them into consideration when splitting into teams.

# Given the masks of the directions the animals are watching, find the minimum possible number of teams the children can form.

# Example

# For

# directions = [[13, 14,  9],
#               [4,   1,  5],
#               [7,  10, 11]]

# the output should be solution(directions) = 1.

# Here's an image showing which paths are not safe:


def solution(d):
    from collections import defaultdict as ddict
    directions = {0: (-1, 0), 1: (0, -1), 2: (1, 0), 3: (0, 1)}
    row, col = len(d), len(d[0])
    g = numpy.zeros((row, col), 'i4')
    node = 0
    f = ddict(set)
    
    for i in range(row):
        for j in range(col):
            g[i, j] = node
            node += 1
    
    for i in range(row):
        for j in range(col):
            tmp = format(d[i][j], 'b').zfill(4)
            for k in range(4):
                if tmp[k] == '0':
                    x, y = directions[k]
                    f[g[i][j]].add(g[i + x][j + y])
    
    def tarjan(node, dis, low):
        global count, time
        dis[node] = low[node] = time
        time += 1
        member[node] = 1
        stack.append(node)
        
        for v in f[node]:
            if dis[v] == -1:
                tarjan(v, dis, low)
                low[node] = min(low[node], low[v])
            elif member[v]:
                low[node] = min(low[node], dis[v])
        
        w = -1
        if low[node] == dis[node]:
            count += 1
            while w != node:
                w = stack.pop()
                member[w] = 0
    
    dis = [-1] * (row * col)
    low = [-1] * (row * col)
    member = [0] * (row * col)
    stack = []
    global count, time
    count = time = 0
    
    for i in range(row * col):
        if dis[i] == -1:
            tarjan(i, dis, low)
    
    return count

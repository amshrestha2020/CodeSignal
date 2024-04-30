# Not long ago you saw an orienteering competition on TV and immediately wanted to try it yourself. You've joined an orienteering club and started preparing for the upcoming competitions.

# One of the most important components of an orienteering competition is running. In order to train this skill you decided to practice on your club's special training field that consists of n locations numbered from 0 to n - 1, with some of them connected by two-way roads of different lengths. There are n roads in total, and any location is reachable from another one by the roads (possibly more than one). Your coach has composed a training route for you that consists of several locations that you should visit in the exact given order. Note, that you may be required to visit some location several times on your training route.

# Given the number of locations n, roads between them and the training route, find the minimum possible total length of this route.

# Example

# For n = 6,

# roads = [[[1, 50], [3, 10], [5, 4]],
#          [[0, 50], [2, 15], [3, 5]], 
#          [[1, 15], [4, 55]], 
#          [[0, 10], [1, 5]],
#          [[2, 55]], 
#          [[0, 4]]]
# and route = [5, 1, 0, 2], the output should be
# solution(n, roads, route) = 64.

# The shortest path between locations numbered 5 and 1 is of length 19, between 1 and 0 it's 15, and between 0 and 2 it's 30. The shortest route length is thus 19 + 15 + 30 = 64.

# Example


def solution(n, roads, route):
    disc = [0]*n
    low = [0]*n
    height = [0]*n
    parent = [0]*n

    # make sure that cheaper edges come first, so in case we have
    # a double edge from one node to another, the cheaper one will win.
    for r in roads:
        r.sort()

    # build spanning tree and assign component IDs (low)
    circumference = 0
    d = 0
    def dfs(v, p):
        nonlocal d, circumference
        low[v] = disc[v] = d + 1
        d += 1
        parent[v] = p
        for r in roads[v]:
            if r[0] != p:
                newlow = disc[r[0]]
                if not newlow:
                    height[r[0]] = height[v] + r[1]
                    dfs(r[0], v)
                    newlow = low[r[0]]
                if newlow <= low[v]:
                    low[v] = newlow
                    circumference += r[1]
    dfs(0, -1)

    total = 0
    for i in range(1, len(route)):
        d = [0, 0]
        s, t = route[i-1], route[i]
        while s != t:
            if height[s] < height[t]:
                s, t = t, s
            d[low[s] == low[parent[s]]] += height[s] - height[parent[s]]
            s = parent[s]

        total += d[0] + min(d[1], circumference - d[1])

    return total

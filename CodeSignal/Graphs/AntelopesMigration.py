# You are the leader of a tribe living on a remote archipelago that consists of several islands connected by bidirectional bridges. Vegetarianism is the main trend of young aborigines of your tribe, and as an old-school man you are certainly not impressed. You decided to show teenagers how exciting hunting could be.

# Every year antelopes migrate from island a to island b (antelopes are not stupid, so they have chosen such a and b that there is at least one path between them). Your troops have prepared a trap, and now you should chose on one of the islands of your archipelago to set it. Migration is a rare event that doesn't last long, so you have only one chance to do this right. All the conversations about lousy vegetables really annoy you, so you want to make sure that the trap will be set in such way that antelopes will definitely fall into it.

# Given the number of islands, the bridges configuration and information about islands a and b, find all the islands lying on every path from a to b. Note, that islands a and b shouldn't be included in the answer, since you won't be able to set a trap unnoticed there and the antelopes will be scared away.

# Example

# For islands = 4,

# bridges = [[0, 1],
#            [1, 2],
#            [2, 0],
#            [2, 3]]
# a = 0, and b = 3, the output should be
# solution(islands, bridges, a, b) = [2].

# Here's an image showing the bridges between the islands:


def solution(islands, bridges, A, B):
    from collections import deque

    # Create an adjacency list for the graph
    adj = [set() for _ in range(islands)]
    for i, j in bridges:
        adj[i].add(j)
        adj[j].add(i)

    # Initialize distances from A and B
    inf = float("inf")
    fromA = [inf] * islands
    toB = [inf] * islands

    # BFS from A
    Q = deque()
    Q.append((A, 0))
    while Q:
        p, d = Q.popleft()
        if fromA[p] < inf:
            continue
        fromA[p] = d
        for nei in adj[p]:
            if fromA[nei] == inf:
                Q.append((nei, d + 1))

    # BFS from B
    Q.append((B, 0))
    while Q:
        p, d = Q.popleft()
        if toB[p] < inf:
            continue
        toB[p] = d
        for nei in adj[p]:
            if toB[nei] == inf:
                Q.append((nei, d + 1))

    # Calculate total distance
    dist = fromA[B]

    # Find candidate nodes
    cands = [i for i in range(islands) if fromA[i] + toB[i] == dist]

    # Create partitions
    partitions = {i: set() for i in range(dist + 1)}
    for c in cands:
        partitions[fromA[c]].add(c)

    # Filter valid nodes
    valids = set()
    for i in range(1, dist):
        if len(partitions[i]) > 1:
            continue
        for x in partitions[i]:
            isGood = True
            for y in partitions[i - 1]:
                if y not in adj[x]:
                    isGood = False
                    break
            if isGood:
                for y in partitions[i + 1]:
                    if y not in adj[x]:
                        isGood = False
                        break
            if isGood:
                valids.add(x)

    # Remove A and B from valid nodes
    valids = list(sorted(valids - {A, B}))

    # Check if a node is necessary
    def isNecessary(node):
        visited = [False] * islands
        visited[node] = True
        stack = [A]
        while stack:
            p = stack.pop()
            if visited[p]:
                continue
            visited[p] = True
            if p == B:
                return False
            for nei in adj[p]:
                if not visited[nei]:
                    stack.append(nei)
        return True

    # Return necessary nodes
    return [x for x in valids if isNecessary(x)]

# Example usage
islands = 5
bridges = [(0, 1), (1, 2), (2, 3), (3, 4)]
A = 0
B = 4
print(solution(islands, bridges, A, B))

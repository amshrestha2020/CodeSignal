# Your company uses local network consisting of n computers some pairs of which are connected by wires. Each wire has its specific speed of data transmission which is the same for both directions. Your boss wants to cut down on the expenses and leave only n - 1 wires. His only concern is that the network should still be connected, so he is willing to get rid of a random wire.

# It pains you to see such a waste: efficiency is at stake! In order to explain your boss how wrong his decision is, you'd like to find the sums of speeds of data transmission along each edge of the most optimal scheme with n - 1 wires, and for the second optimal one. The difference between them should convince your boss how important efficiency is, so that is what the function you need to implement should find.

# Example

# For n = 4
# and

# wires = [[1, 2, 1], 
#          [1, 4, 3], 
#          [2, 3, 3],
#          [2, 4, 2],
#          [3, 4, 4]]
# the output should be
# solution(n, wires) = 1.

# The most optimal scheme contains wires between three pairs of computers (1 and 2, 2 and 4, and 2 and 3), with the total speed equal to 6. The second optimal scheme contains wires between computers 1 and 2, 2 and 4, and 3 and 4, summing up to the total speed of 7.


def solution(n, wires):
    parent = list(range(n + 1))
    rank = [0] * (n + 1)
    edges = sorted((w, u, v) for u, v, w in wires)

    def find(x):
        if parent[x] != x:
            parent[x] = find(parent[x])
        return parent[x]

    def union(x, y):
        x_root = find(x)
        y_root = find(y)
        if rank[x_root] < rank[y_root]:
            parent[x_root] = y_root
        elif rank[x_root] > rank[y_root]:
            parent[y_root] = x_root
        else:
            parent[y_root] = x_root
            rank[x_root] += 1

    def kruskal(edge_to_remove):
        for i in range(1, n + 1):
            parent[i] = i
            rank[i] = 0
        total_weight = 0
        mst_edges = []
        for w, u, v in edges:
            if (u, v) == edge_to_remove or (v, u) == edge_to_remove:
                continue
            if find(u) != find(v):
                union(u, v)
                total_weight += w
                mst_edges.append((u, v))
        return total_weight, mst_edges

    mst_weight, mst_edges = kruskal(None)
    min_diff = float('inf')
    for edge in mst_edges:
        weight, _ = kruskal(edge)
        if weight >= mst_weight:
            min_diff = min(min_diff, weight - mst_weight)

    return min_diff

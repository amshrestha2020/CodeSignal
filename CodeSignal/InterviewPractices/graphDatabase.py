# You have a strongly connected directed graph that has positive weights in the adjacency matrix g. The graph is represented as a square matrix, where g[i][j] is the weight of the edge (i, j), or -1 if there is no such edge.

# Given g and the index of a start vertex s, find the minimal distances between the start vertex s and each of the vertices of the graph.

# Example

# For

# g = [[-1, 3, 2],
#      [2, -1, 0],
#      [-1, 0, -1]]
# and s = 0, the output should be
# solution(g, s) = [0, 2, 2].

# Example

# The distance from the start vertex 0 to itself is 0.
# The distance from the start vertex 0 to vertex 1 is 2 + 0 = 2.
# The distance from the start vertex 0 to vertex 2 is 2.


def solution(g, s):
    n = len(g)
    INF = float('inf')
    distances = [INF] * n
    distances[s] = 0
    visited = set()

    while len(visited) < n:
        min_distance = INF
        min_vertex = -1
        for v in range(n):
            if v not in visited and distances[v] < min_distance:
                min_distance = distances[v]
                min_vertex = v

        visited.add(min_vertex)

        for neighbor in range(n):
            if g[min_vertex][neighbor] != -1:
                new_distance = distances[min_vertex] + g[min_vertex][neighbor]
                if new_distance < distances[neighbor]:
                    distances[neighbor] = new_distance

    return distances

# Example usage:
g = [[-1, 3, 2],
     [2, -1, 0],
     [-1, 0, -1]]
s = 0
print(solution(g, s))  # Output: [0, 2, 2]

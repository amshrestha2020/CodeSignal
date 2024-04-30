# In order to protect your office from intruders, your boss decided to install a high-tech lock on the door. The lock represents a large cube with some points floating inside. When the correct pin is entered, the points start to connect to each other by rays of light until they form a single connected structure with rays of the minimum possible total length. When this happens, the lock opens.

# Your boss likes interesting challenges, but is not very fond of solving them himself. This is why he asked you, his most (or least?) favorite employee, to solve the challenge he came up with. Given the set of points, he wants you to find the optimal structure that opens the lock. Since there can be several optimal structures, your task is to return the minimum total length of all the rays in one of such structures.

# Example

# For points = [[0, 0, 0], [1, 1, 1], [1, -1, 1], [-1, 1, 1], [-1, -1, -1]],
# the output should be
# solution(points) = 6.9282032303.

# The best way is to connect point [0, 0, 0] with all other points.


import math

class DisjointSet:
    def __init__(self, n):
        self.parent = list(range(n))
        self.rank = [0] * n

    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, x, y):
        root_x = self.find(x)
        root_y = self.find(y)
        if root_x == root_y:
            return False
        if self.rank[root_x] < self.rank[root_y]:
            self.parent[root_x] = root_y
        elif self.rank[root_x] > self.rank[root_y]:
            self.parent[root_y] = root_x
        else:
            self.parent[root_y] = root_x
            self.rank[root_x] += 1
        return True

def distance(point1, point2):
    return math.sqrt((point1[0] - point2[0])**2 + (point1[1] - point2[1])**2 + (point1[2] - point2[2])**2)

def solution(points):
    edges = []
    n = len(points)
    for i in range(n):
        for j in range(i + 1, n):
            edges.append((distance(points[i], points[j]), i, j))
    edges.sort()
    
    disjoint_set = DisjointSet(n)
    total_length = 0
    num_edges_added = 0
    
    for edge in edges:
        length, vertex1, vertex2 = edge
        if disjoint_set.union(vertex1, vertex2):
            total_length += length
            num_edges_added += 1
            if num_edges_added == n - 1:
                break
    
    return total_length

# Example usage:
points = [[0, 0, 0], [1, 1, 1], [1, -1, 1], [-1, 1, 1], [-1, -1, -1]]
print(solution(points))  # Output: 6.928203230275509

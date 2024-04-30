# As a director of a large company, you try to do your best to make the working environment as efficient as possible. However, it's difficult to do so when even the hardware used in the office is not efficient: there are too many wires connecting your employees' computers.

# Naturally, you decided to minimize their number by getting rid of some wires. There's only one constraint: if it is possible to deliver information from one computer to another one using the wires, it should still be possible to do so after the renovation. You would also like to minimize the total wires length, because the longer the wires, the more it possible for you to trip over them at some point.

# Given the plan of your n office computers and the wires connecting them, find the minimum resulting length of the wires after removing some of them according to the constraints above.

# Example

# For n = 7 and

# wires = [[0, 1, 1], [2, 0, 2], [1, 2, 3], [3, 4, 1],
#          [4, 5, 2], [5, 6, 3], [6, 3, 2]]
# the output should be solution(n, wires) = 8.



# The best way is to remove wires 3 and 6 (1-based).



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

def solution(n, wires):
    wires.sort(key=lambda x: x[2])  # Sort wires by length
    disjoint_set = DisjointSet(n)
    min_wire_length = 0
    for wire in wires:
        computer1, computer2, length = wire
        if disjoint_set.union(computer1, computer2):
            min_wire_length += length
    return min_wire_length

# Example usage:
n = 7
wires = [[0, 1, 1], [2, 0, 2], [1, 2, 3], [3, 4, 1], [4, 5, 2], [5, 6, 3], [6, 3, 2]]
print(solution(n, wires))  # Output: 8

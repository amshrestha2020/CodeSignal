# Not long ago your best programmer retired. He was the best programmer in the town, and now there is no one in the company who can take his place. As a director and a former programmer, you decided to take his place for a while.

# Your company is really big and has n its very own servers and a lot of wires of different lengths connecting them. Of course, the information can be delivered from any server to any other one. Now you should remove some of the wires so that:

# information can still be delivered from any server to any other one;
# the total length of the remaining wires is as small as possible.
# Years of office work did leave their mark, so you're not sure if you can handle the task right away. To begin with, you decided to start off by finding k wires of the minimal length that will definitely be left after you remove some of the excessive wires. This little cheat helped you to write a script that returns a list of wires that should be removed.

# However, it turned out that removing excessive wires is no yet possible because of other more pressing matters, so you keep putting the task off. The problem is, when the time passes, some of the wires break down and are replaced by the new ones. Each time such an update occurs, you have to recalculate the result. You're naturally not too happy about this, so you would like to write a program that will do the job for you.

# Given the list of updates containing the information about the wires replacements, for each update calculate the total length of the k shortest wires that shouldn't be removed as excessive according to the constraints above.

# Example

# For n = 4, wires = [[0, 1, 1], [1, 2, 2], [2, 3, 3], [3, 0, 4]],
# k = 3, and updates = [[0, 1, 5], [3, 0, 2]], the output should be
# solution(n, wires, k, updates) = [9, 7].

from collections import defaultdict
from bisect import insort
import numpy

def solution(n, wires, k, updates):
    parent = list(range(n))
    rank = [0] * n
    queue = []
    res = []
    d = defaultdict(dict)

    def find(node):
        if parent[node] != node:
            parent[node] = find(parent[node])
        return parent[node]

    def union(x, y):
        if rank[x] > rank[y]:
            x, y = y, x
        parent[x] = y
        rank[x] += rank[y] + 1

    for i, j, w in wires:
        insort(queue, [w, i, j])
        d[i][j] = d[j][i] = w

    for x, y, weight in updates:
        insort(queue, [weight, x, y])
        d[x][y] = d[y][x] = weight
        v = s = count = 0
        rank = defaultdict(int)
        parent = numpy.arange(n)
        while count < k:
            w, i, j = queue[v]
            if w == d[i][j]:
                if find(i) != find(j):
                    s += w
                    count += 1
                    union(i, j)
            v += 1
        res.append(s)

    return res

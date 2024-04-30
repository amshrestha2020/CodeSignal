# Not long ago you discovered a wonderful tree in the nearby woods that made you very curious about the greenery around you. You went to the nearby woods and drew various plants in your notebook. The plants in the woods have various structures: some of them even contain loops!

# Anyway, for now you are interested only in trees. You came up with a brand new property: you call a tree a caterpillar if there exists a path in it, such that each vertex of a tree either belongs to this path or is connected to one of its vertices by a single edge. To find out more about them, you would like to write a program that will find all interesting trees in the structures you drew in your notebook.

# The plants you drew consist of n vertices and are connected by several edges. Calculate the number of regular trees and caterpillar trees in the structures you drew in your notebook.

# Example

# For n = 21 and

# edges = [[0, 1], [1, 2], [2, 3], [2, 4], [4, 5], [4, 6], [4, 7],
#          [4, 8], [4, 9], [4, 10], [10, 11], [11, 12], [11, 13],
#          [11, 14], [14, 15], [14, 16], [14, 17], [14, 18], [14, 19]]
# the output should be solution(n, edges) = [2, 2].



# There are two connected components and both of them are trees and caterpillar trees.

# For n = 22 and

# edges = [[0, 1], [1, 2], [2, 3], [2, 4], [4, 5], [4, 6], [4, 7],
#          [4, 8], [4, 9], [4, 10], [10, 11], [11, 12], [11, 13],
#          [11, 14], [14, 15], [14, 16], [14, 17], [14, 18], [14, 19], [13, 20]]
# the output should be solution(n, edges) = [2, 1].



# The first connected component is a tree, but not a caterpillar tree, because vertex 20 is not directly connected to the central path.


from collections import defaultdict

def solution(n, edges):
    G = defaultdict(set)
    for u, v in edges:
        G[u].add(v)
        G[v].add(u)

    ans0 = ans1 = 0

    seen = set()
    for i in range(n):
        if i in seen:
            continue
        stack = [i]
        saw = {i}
        while stack:
            node = stack.pop()
            for nei in G[node]:
                if nei not in saw:
                    saw.add(nei)
                    stack.append(nei)

        seen |= saw

        if sum(len(G[node]) for node in saw) + 2 == len(saw) * 2:
            ans0 += 1
            for node in set(saw):
                if len(G[node]) == 1:
                    saw.discard(node)

            ans1 += all(len(G[node] & saw) <= 2 for node in saw)

    return ans0, ans1

# You are the leader of a tribe living on an archipelago. Traditionally, each year your tribe organizes a parade to demonstrate the might of your tribal army. During this parade the procession goes from island to island via one-way bridges. The parade starts and finishes in the capital, located on island 1. Each parade has its own representation that describes the route of the parade as an array of bridges in the order they are crossed, where each bridge given by its construction year.

# This year you'd like to prepare an ideal parade. The parade is ideal if the marching army traverses each bridge exactly once (although it can visit the same island multiple times) and its representation is lexicographically smallest among all such parades.

# You would like the parade to go without a hitch, so you need to plan in advance the location of the parade at each given moment of time, assuming that it takes 1 unit of time to cross a bridge. Given the number of islands n and arrays of bridges and times, return the island on which the processing will be in each given moment of time, or an empty array if ideal parade is not even possible.

# Example

# For n = 5,

# bridges = [[1, 2, 500],
#             [1, 5, 1000],
#             [2, 3, 2000],
#             [3, 1, 2016],
#             [4, 1, 1900],
#             [5, 4, 2012]]
# and

# times = [0, 1, 2, 3, 4, 5, 6]
# the output should be
# solution(n, bridges, times) = [1, 2, 3, 1, 5, 4, 1];

# For n = 3,

# bridges = [[1, 2, 500],
#             [1, 3, 1000],
#             [2, 3, 2000]]
# and

# times = [0, 1, 2]
# the output should be
# solution(n, bridges, times) = [].

# It's impossible to organize an ideal parade.


def solution(n, bridges, times):
    path = [1]
    circuit = []
    graph = [[] for _ in range(n + 1)]
    balance = [0] * n
    cur = 1

    for u, v, w in bridges:
        graph[u].append((v, w))
        balance[u - 1] += 1
        balance[v - 1] -= 1

    graph = [sorted(adj, key=lambda x: x[1]) for adj in graph]

    if any(balance):
        return []

    while path:
        if graph[cur]:
            path.append(cur)
            cur = graph[cur].pop(0)[0]
        else:
            circuit.insert(0, cur)
            cur = path.pop()

    return [circuit[time] for time in times]

# Example usage:
n = 5
bridges = [[1, 2, 500],
           [1, 5, 1000],
           [2, 3, 2000],
           [3, 1, 2016],
           [4, 1, 1900],
           [5, 4, 2012]]
times = [0, 1, 2, 3, 4, 5, 6]
print(solution(n, bridges, times))  # Output: [1, 2, 3, 1, 5, 4, 1]

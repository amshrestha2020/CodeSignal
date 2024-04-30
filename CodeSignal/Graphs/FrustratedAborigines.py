# You are the leader of a tribe living on a remote archipelago. It consists of several islands connected by bridges. All the bridges of your archipelago are narrow, so people often run into each other and fall into the water. To end this once and for all, you decided to make the traffic on all bridges go one-way.

# You issued the corresponding decree as soon as this brilliant idea came to your mind, but unfortunately there is a problem: for some people some islands are now unreachable, which is quite frustrating for your subjects. To measure frustration of your tribe, you'd like to calculate the number of pairs (aborigine, island) such that the aborigine can't reach the island.

# Given the number of people on each island crowd and the map of the bridges, find frustrations of the aborigines.

# Example
# For

# bridges = [[1],
#            [2],
#            [1]]
# and crowd = [4, 1, 2],
# the output should be solution(bridges, crowd) = 3.

# Here's how your archipelago looks like:



# All the aborigines from the 1st and 2nd islands can't reach the 0th island.


def dfs(island, bridges, visited):
    visited[island] = True
    for neighbor in bridges[island]:
        if not visited[neighbor]:
            dfs(neighbor, bridges, visited)

def solution(bridges, crowd):
    n = len(bridges)
    unreachable_count = 0
    for i in range(n):
        visited = [False] * n
        dfs(i, bridges, visited)
        for j in range(n):
            if crowd[i] > 0 and not visited[j]:
                unreachable_count += crowd[i]
    return unreachable_count

# Test the example
bridges = [[1], [2], [1]]
crowd = [4, 1, 2]
print(solution(bridges, crowd))  # Output should be 3

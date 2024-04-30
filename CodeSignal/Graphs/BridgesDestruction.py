# You are the son of the leader of a tribe living on a remote archipelago. It consists of several islands connected by bidirectional bridges. You think your father is too old to be a leader, and would like to prove it to others. The Council of Elders will be convened tomorrow, and this is your best chance to show that the things don't go as well as they used to when your father was young.

# You decided to destroy one bridge of the archipelago (they are too strong, so you don't have enough time to destroy several bridges). All elders live on the island a, and the council will take place on the island b. You want to make sure that the elders see the destruction, so you need to destroy such a bridge that lies on the path between a and b. This is your only chance, so the bridge should belong to each path between a and b.

# As the first step you want to calculate the number of suitable bridges. Given the bridges configuration and information about islands a and b, return the number of bridges which destruction will definitely be noted by the elders.

# Example

# For

# bridges = [[1, 2],
#            [0],
#            [0]]
# a = 0, and b = 2,
# the output should be solution(bridges, a, b) = 1.

# Here's an image showing the bridges between the islands:


def solution(bridges, a, b):
    k = len(bridges)
    g = set()
    visited, low, dis, parent, time = [0] * k, [0] * k, [0] * k, [-1] * k, [0]
    
    def dfs(node):
        visited[node] = 1
        low[node] = dis[node] = time[0]
        time[0] += 1
        
        for v in bridges[node]:
            if not visited[v]:
                parent[v] = node
                dfs(v)
                low[node] = min(low[node], low[v])
                if low[v] > dis[node]:
                    g.add((v, node))
            else:
                if parent[node] != v:
                    low[node] = min(low[node], dis[v])
    
    dfs(a)
    ancestor = {a, b}
    
    while b != -1:
        ancestor.add(parent[b])
        b = parent[b]
    
    return sum(p in ancestor and q in ancestor for p, q in g)

# Example usage:
bridges = [[1, 2], [0], [0]]
a = 0
b = 2
result = solution(bridges, a, b)
print(f"Number of suitable bridges: {result}")

# You got sick because of walking in the woods at night, and have to spend a week at home without going out. Looking out of the window at the nearby woods you're wondering if there is anything you don't yet know about them. Suddenly you see a beautiful and very tall tree you haven't seen before. Since you have nothing to do, you decide to examine its structure and draw it in your notebook.

# You became so exited about this new tree that your temperature went up, so you were forced to stay in bed. You can't see the tree from your bed, but luckily you have it drawn down. The first thing you'd like to find out about is the tree height. Looking at your drawing you suddenly realize that you forgot to mark the tree bottom and you don't know from which vertex you should start counting. Of course a tree height can be calculated as the length of the longest path in it (it is also called tree diameter). So, now you have a task you need to solve, so go ahead!

# Example

# For n = 10 and

# tree = [[2, 5], [5, 7], [5, 1], [1, 9], [1, 0], [7, 6], [6, 3], [3, 8], [8, 4]]
# the output should be solution(n, tree) = 7.



# The longest path is the path from vertex 4 to one vertex 9 or 0.


from collections import defaultdict

def dfs(node, graph, visited, dist):
    visited[node] = True
    for neighbor in graph[node]:
        if not visited[neighbor]:
            dist[neighbor] = dist[node] + 1
            dfs(neighbor, graph, visited, dist)

def solution(n, tree):
    # Create an adjacency list representation of the tree
    graph = defaultdict(list)
    for u, v in tree:
        graph[u].append(v)
        graph[v].append(u)
    
    # Perform the first DFS to find the farthest vertex from any starting vertex
    visited = [False] * n
    dist = [0] * n
    dfs(0, graph, visited, dist)
    
    # Find the farthest vertex from the starting vertex
    u = dist.index(max(dist))
    
    # Reset visited and dist arrays for the second DFS
    visited = [False] * n
    dist = [0] * n
    
    # Perform the second DFS to find the farthest vertex from the farthest vertex found in the first DFS
    dfs(u, graph, visited, dist)
    
    # Return the maximum distance found
    return max(dist)

# Test case
print(solution(10, [[2, 5], [5, 7], [5, 1], [1, 9], [1, 0], [7, 6], [6, 3], [3, 8], [8, 4]]))  # Output: 7

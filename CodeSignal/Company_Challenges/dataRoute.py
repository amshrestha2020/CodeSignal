# Two Sigma's mission is to uncover value in the world's data, and as part of that it's necessary to download massive amounts of information on a regular basis. Naturally, this data should be transferred as quickly and efficiently as possible.

# A new data resource was recently added to the network, and your job is to establish a connection between it and Two Sigma's server. Due to security reasons, all connections in Two Sigma's network are unidirectional (i.e. only have a one-way connection), and no data can be stored on any node of the network. This means that every second the amount of data a node receives should be equal to the amount of data it forwards. The only exceptions to this rule are resource and server, since the former only sends data while the latter only receives it.

# Unfortunately, some segments of the network are slower than is ideal due to limitations with legacy telecommunication operators around the world. This complicates finding the optimal route through the network significantly, which is why your help is required.

# Find a route between the resource and the server that maximizes the amount of data downloaded in a second, and return this maximum value.

# Example

# For resource = 4, server = 5, and

# network = [[0, 2, 4, 8, 0, 0],
#            [0, 0, 0, 9, 0, 0],
#            [0, 0, 0, 0, 0, 10],
#            [0, 0, 6, 0, 0, 10],
#            [10, 10, 0, 0, 0, 0],
#            [0, 0, 0, 0, 0, 0]]
# the output should be solution(resource, server, network) = 19.

# Here's what the network looks like:


# And here's how data should be transfered within it:


# Input/Output

# [execution time limit] 4 seconds (py3)

# [memory limit] 1 GB

# [input] integer resource

# A 0-based index of the resource node.

# Guaranteed constraints:
# 0 ≤ resource < 15.

# [input] integer server

# A 0-based index of the server node.

# Guaranteed constraints:
# 0 ≤ server < 15,
# server ≠ resource.

# [input] array.array.integer network

# A square matrix of non-zero elements. network[i][j] corresponds to the maximum amount of data that can be transfered from the ith to the jth node in one second, in megabytes.

# Note that although all connections go only one way, there can be two routes between two nodes a and b, one transferring data from a to b and another one from b to a.

# Guaranteed constraints:
# 2 ≤ network.length ≤ 15,
# network[i].length = network.length,
# 0 ≤ network[i][j] ≤ 105,
# network[i][i] = 0.

# [output] integer

# The maximum amount of data that can be transferred in one second, in megabytes.


def solution(resource, server, network):
    # Create a residual graph and fill it with given capacities
    residual_graph = [row[:] for row in network]
    parent = [-1] * len(network)
    max_flow = 0

    # Augment the flow while there is a path from resource to server
    while bfs(residual_graph, resource, server, parent):
        # Find the maximum flow through the path found
        path_flow = float("Inf")
        s = server
        while s != resource:
            path_flow = min(path_flow, residual_graph[parent[s]][s])
            s = parent[s]

        # Update the residual capacities of the edges and reverse edges
        v = server
        while v != resource:
            u = parent[v]
            residual_graph[u][v] -= path_flow
            residual_graph[v][u] += path_flow
            v = parent[v]

        # Add path flow to the overall flow
        max_flow += path_flow

    # Return the maximum flow
    return max_flow

def bfs(residual_graph, source, sink, parent):
    # Create a visited array and mark all nodes as not visited
    visited = [False] * len(residual_graph)

    # Create a queue, enqueue the source node, and mark it as visited
    queue = [source]
    visited[source] = True

    # Standard BFS loop
    while queue:
        u = queue.pop(0)

        # If we found the sink node in BFS starting from source, then return True
        if u == sink:
            return True

        # Otherwise, go through all adjacent vertices
        for ind, val in enumerate(residual_graph[u]):
            if not visited[ind] and val > 0:
                queue.append(ind)
                visited[ind] = True
                parent[ind] = u

    # If we reached here, then there is no path from source to sink
    return False

# You decided to create an automatic image recognizer that will determine the object in the image based on its contours. The main recognition system is already implemented, and now you need to start the teaching process.

# Today you want to teach your program to recognize star patterns in the image of the night sky, which means that you need to implement a function that, given the adjacency matrix representing a number of contours in the sky, will find the number of stars in it.

# The graph representing some contour is cosidered to be a star if it is a tree of size 2 or if it is a tree of size k > 2 with one internal node (which is a tree root at the same time) and k - 1 leaves.
# Here is an example of some stars:

# Stars

# Given the sky objects' contours as an undirected graph represented by its adjacency matrix adj, calculate the number of stars in it.

# Example

# For

# adj = [[false, true, false, false, false],
#        [true, false, false, false, false],
#        [false, false, false, true, false],
#        [false, false, true, false, false],
#        [false, false, false, false, false]]
# the output should be
# solution(adj) = 2.

# Here's what the given graph looks like:

# Example


def solution(edges):
    # Number of nodes in the graph
    num_nodes = len(edges)
    
    # Degree of each node (number of edges connected to the node)
    degrees = [sum(edge) for edge in edges]
    
    # Initialize the count of stars
    star_count = 0
    
    # Iterate over each node
    for i in range(num_nodes):
        # If the node is not connected to itself and all its connected nodes have degree 1
        if edges[i][i] == False and all(degrees[v] == 1 for v in range(num_nodes) if edges[i][v]):
            # If the node has more than one connection, increment the count of stars
            # If the node has only one connection, increment the count of stars by 0.5
            star_count += 1 if degrees[i] > 1 else 0.5 * degrees[i]
    
    return star_count

# You decided to create an automatic image recognizer that will determine the object in the image based on its contours. The main recognition system is already implemented, and now you need to start the teaching process.

# Today you want to teach your program to recognize wheel patterns, which means that you need to implement a function that, given the adjacency matrix representing the contour, will determine whether it's a wheel or not.

# The wheel contour can be thought of as a single center vertex and a regular polygon with n (n > 2) vertices which are all connected to the center. Here is an example:

# A wheel

# Given the object's contour as an undirected graph represented by its adjacency matrix adj determine whether it's a wheel or not.

# Example

# For

# adj = [[false, true, true, true, true],
#        [true, false, true, false, true],
#        [true, true, false, true, false],
#        [true, false, true, false, true],
#        [true, true, false, true, false]]
# the output should be
# solution(adj) = true.

# Here's what the given graph looks like:

# Example


def solution(adj):
    vertex_count = len(adj)
    degree_sequence = sorted(sum(row) for row in adj)
    no_self_loops = all(adj[i][i] == False for i in range(vertex_count))

    return degree_sequence == [3] * (vertex_count - 1) + [vertex_count - 1] and no_self_loops

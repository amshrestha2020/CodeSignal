# You decided to create an automatic image recognizer that will determine the object in the image based on its contours. The main recognition system is already implemented, and now you need to start the teaching process.

# Today you want to teach your program to recognize book patterns, which means that you need to implement a function that, given the adjacency matrix representing the contour, will determine whether it's a book or not.

# A book consists of a base and may have any number of pages.
# The book's base consists of a single edge connecting two nodes, and it is a common edge for all the pages. Besides that, every page has only one node connected to both sides of the base.
# Here is an example of a book:

# Book

# Given the object's contour as an undirected graph represented by its adjacency matrix adj determine whether it's a book or not.

# Example

# For

# adj = [[false, true, true, true],
#        [true, false, true, true],
#        [true, true, false, false],
#        [true, true, false, false]]
# the output should be
# solution(adj) = true.

# Here's how the given graph looks like:

# Example

def solution(adj):
    vertex_count = len(adj)
    degree_sequence = sorted(sum(row) for row in adj)
    no_self_loops = all(adj[i][i] == False for i in range(vertex_count))

    return degree_sequence == [2] * (vertex_count - 2) + [vertex_count - 1] * 2 and no_self_loops


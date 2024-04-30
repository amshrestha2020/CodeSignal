# You decided to create an automatic image recognizer that will determine the object in the image based on its contours. The main recognition system is already implemented, and now you need to start the teaching process.

# Today you want to teach your program to recognize tadpole patterns, which means that you need to implement a function that, given the adjacency matrix representing the contour, will determine whether it's a tadpole or not.

# The tadpole contour consists of two parts: a head which is a cycle with n (n > 2) vertices, and a tail which is a simple path (with at least one vertex) connected to the head. Here is an example:

# A tadpole

# Given the object's contour as an undirected graph represented by its adjacency matrix adj determine whether it's a tadpole or not.

# Example

# For

# adj = [[false, true, true, false, false],
#        [true, false, false, true, false],
#        [true, false, false, true, false],
#        [false, true, true, false, true],
#        [false, false, false, true, false]]
# the output should be
# solution(adj) = true.

# Here's what the given graph looks like:

# Example


def solution(adj):
    return solutionSignature(adj) and isConnected(adj)


def solutionSignature(adj):
    return sorted(sum(row) for row in adj) == [1] + [2] * (len(adj) - 2) + [3]


def isConnected(adj):
    removeConnectedTrues(adj, 0)
    return not any(any(row) for row in adj)


def removeConnectedTrues(adj, j):
    for i in range(len(adj)):
        if adj[i][j]:
            adj[i][j] = adj[j][i] = False
            removeConnectedTrues(adj, i)

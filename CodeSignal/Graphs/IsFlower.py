# You decided to create an automatic image recognizer that will determine the object in the image based on its contours. The main recognition system is already implemented, and now you need to start the teaching process.

# Today you want to teach your program to recognize flower patterns, which means that you need to implement a function that, given the adjacency matrix representing the contour, will determine whether it's a flower or not.

# The flower contour consists of several (at least one) petals.
# Petal contours are the same-sized (of size greater than 2) complete graphs with exactly one common vertex.
# Here are some examples of the flower contours:

# flowers

# Given the object's contour as an undirected graph represented by adjacency matrix adj determine whether it's a flower or not.

# Example

# For

# adj = [[false, true, true, true, true],
#        [true, false, true, false, false],
#        [true, true, false, false, false],
#        [true, false, false, false, true],
#        [true, false, false, true, false]]
# the output should be
# solution(adj) = true.

# Here's what the given graph looks like:

# Example


def solution(adjacency_matrix):
    petal_rank, has_flower_signature = check_flower_signature(adjacency_matrix)
    return has_flower_signature and not has_self_connections(adjacency_matrix) and count_petals(adjacency_matrix) * petal_rank == len(adjacency_matrix) - 1

def has_self_connections(adjacency_matrix):
    return any(adjacency_matrix[i][i] for i in range(len(adjacency_matrix)))

def check_flower_signature(adjacency_matrix):
    degree_counts = sorted(sum(row) for row in adjacency_matrix)
    petal_rank = degree_counts[0]
    return petal_rank, petal_rank >= 2 and degree_counts[-1] == len(adjacency_matrix) - 1 and all(petal_rank == count for count in degree_counts[:-1])

def count_petals(adjacency_matrix):
    remove_center(adjacency_matrix)
    petal_count = 0
    for i, row in enumerate(adjacency_matrix):
        if any(row):
            petal_count += 1
            remove_connected_edges(adjacency_matrix, i)
    return petal_count

def remove_center(adjacency_matrix):
    center = max(range(len(adjacency_matrix)), key=lambda i: sum(adjacency_matrix[i]))
    for i in range(len(adjacency_matrix)):
        adjacency_matrix[center][i] = adjacency_matrix[i][center] = False

def remove_connected_edges(adjacency_matrix, vertex_index):
    for i in range(len(adjacency_matrix)):
        if adjacency_matrix[i][vertex_index]:
            adjacency_matrix[i][vertex_index] = adjacency_matrix[vertex_index][i] = False
            remove_connected_edges(adjacency_matrix, i)

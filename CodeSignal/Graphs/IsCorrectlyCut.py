# You decided to create an automatic image recognizer that will determine the object in the image based on its contours. The main recognition system is already implemented, and you have taught it to recognized several patterns.

# You are pretty pleased with your results so far and as such you have finally decided to put your program to good use. The timing is perfect: you've received an offer from a jewelery shop. They want you to help them sort their diamonds. Each gem has a different type of a cut which influences its price. You were asked to find all the diamonds with the specific kind of pattern.

# Luckily, your image recognizer has almost everything it takes to tackle the problem,and all that is left for you it is to teach it to recognize correct patterns. You need to implement a function that, given the adjacency matrix representing the cut contour, will determine whether it's a correct or not.

# The pattern of the cut of size 2 · n is a correct one if its contour can be split into two equal groups U and V of n vertices numbered from 0 to n - 1 (in each group) such that for any pair of vertices u and v there exists an edge between them if and only if they don't belong to the same group and their respective "group" numbers are different.

# Here are some examples of correct cut contours (vertices belonging to the same group have the same color).

# Diamonds

# Given the gem's contour as an undirected graph represented by its adjacency matrix adj determine whether it has a correct cut or not.

# Example

# For

# adj = [[false, true, false, false, false, true],
#        [true, false, true, false, false, false],
#        [false, true, false, true, false, false],
#        [false, false, true, false, true, false],
#        [false, false, false, true, false, true],
#        [true, false, false, false, true, false]]
# the output should be
# solution(adj) = true.

# Here's how the given graph looks like (here gn stands for the vertex number in its group):

# Example


def solution(adj):
    all_neighbors = [set(j for j, is_neighbor in enumerate(row) if is_neighbor) for row in adj]
    for neighbors in all_neighbors:
        second_degree_neighbors = set()
        for neighbor in neighbors:
            second_degree_neighbors |= all_neighbors[neighbor]

        if neighbors & second_degree_neighbors or len(neighbors | second_degree_neighbors) != len(adj) - 1:
            return False

    return True


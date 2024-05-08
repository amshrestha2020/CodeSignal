# Consider a big city located on n islands. There are bridges connecting the islands, but they all have only one-way traffic. To make matters worse, most of the bridges are closed at night, so there is at most one bridge with traffic going from any island A to any other island B.

# There is a programmer who turns a penny by working nights as an Uber driver. One night his phone dies right after he picks up a rider going from island 0 to island (n - 1). He has the map of the city bridges in his laptop though (stored as a matrix of distances), so he decides to implement an algorithm that calculates the shortest path between those two islands and evaluate the cost based on the distance of the path. Assume that each mile of the trip is 1$.

# Example

# For

# city = [[-1, 5, 20],
#         [21, -1, 10],
#         [-1, 1, -1]]
# the output should be solution(city) = 15.

# city[i][j] equals the distance between the ith and the jth islands in miles, or -1 if there is no bridge by which one can move from island i to island j.

# solution(city) should be 15, since the shortest distance from the 0th to the 2nd island is 15. The distance from the 0th to the 1st is city[0][1] = 5, and from the 1st to the 2nd is city[1][2] = 10.



# For

# city = [[-1, 5, 2, 15],
#         [2, -1, 0, 3],
#         [1, -1, -1, 9],
#         [0, 0, 0, -1]]
# the output should be solution(city) = 8.

# The shortest path is 0 -> 1 -> 3 which costs 5 + 3 = 8.



# Input/Output

# [execution time limit] 4 seconds (py3)

# [memory limit] 1 GB

# [input] array.array.integer city

# The city is represented as a square matrix, where city[i][j] equals the distance between the ith and the jth islands in miles, or -1 if there is no bridge that allows moving in that direction.

# Guaranteed constraints:
# 2 ≤ city.length ≤ 10,
# city[i].length = city.length,
# -1 ≤ city[i][j] ≤ 30.

# [output] integer

# The cost of the trip. It is guaranteed that there is a route from the 0th to the (n - 1)th island.

def solution(city):
    n = len(city)
    # Initialize the distance matrix with infinity
    dist = [[float('inf')] * n for _ in range(n)]
    
    # Set the distance from each island to itself to 0
    for i in range(n):
        dist[i][i] = 0
    
    # Update the distance matrix with the given distances
    for i in range(n):
        for j in range(n):
            if city[i][j] != -1:
                dist[i][j] = city[i][j]
    
    # Use the Floyd-Warshall algorithm to find the shortest distances between all pairs of islands
    for k in range(n):
        for i in range(n):
            for j in range(n):
                dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])
    
    # Return the shortest distance from island 0 to island (n - 1)
    return dist[0][n - 1]

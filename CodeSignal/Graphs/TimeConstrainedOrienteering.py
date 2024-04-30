# Not long ago you saw an orienteering competition on TV and immediately wanted to try it yourself. You've joined an orienteering club and started preparing for the upcoming competitions. You liked participation so much that you decided to organize your very own competition, and an unusual one.

# In this race the participants should find such a path from start to finish that they will spend no more than T minutes on each road. When a participant leaves a location, the time on their stopwatch is set to T, and the countdown begins. If they can't make it to the next location in T seconds, they lose the race.

# You have already picked a location for the start, but not yet settled for the finish. To decide which location to choose, for each of the n locations you'd like to calculate the minimum value of T that makes it possible to complete the race from start to this location.

# Given the start location, the number of locations n and the roads connecting them, return the number of different minimum possible value of T for every finish location.

# Example

# For n = 5, start = 3, and

# roads = [[1, 2, 3],
#          [2, 3, 1],
#          [2, 4, 2],
#          [3, 5, 4],
#          [4, 5, 3]]
# the output should be
# solution(n, start, roads) = 4.

# The minimum possible values of T for locations from 1 to n are 3, 1, 0, 2 and 3 respectively, 4 distinct values in total.

# Here's how the locations are connected:


import heapq

def solution(n, start, roads):
    # Create an adjacency list from the roads
    adjacency_list = [[] for _ in range(n+1)]
    for road in roads:
        loc1, loc2, t = road
        adjacency_list[loc1].append((loc2, t))
        adjacency_list[loc2].append((loc1, t))

    # Initialize the distance array and the priority queue
    distance = [float('inf')] * (n+1)
    distance[start] = 0
    queue = [(0, start)]  # (distance, node)

    while queue:
        current_distance, current_node = heapq.heappop(queue)
        if current_distance != distance[current_node]:
            continue
        for neighbor, weight in adjacency_list[current_node]:
            new_distance = max(current_distance, weight)
            if new_distance < distance[neighbor]:
                distance[neighbor] = new_distance
                heapq.heappush(queue, (new_distance, neighbor))

    # Return the number of distinct minimum possible values of T
    return len(set(distance[1:]))


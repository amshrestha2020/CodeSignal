# You've just become a director of a big company. As it turned out, the company favors one-on-one meetings, which is why there are so many of them each week. Each meeting has an integer efficiency value that shows how much profit it gives the company. In order to make your employees chat less and work more, you'd like remove some one-on-one's from the weekly schedule and leave as few meetings as possible. Of course, there are some restrictions:

# it should still be possible to deliver information from any employee to any other one (probably, it'll take a bunch of meetings to deliver a piece of information from one worker to the other one);
# there should be as few meetings left as possible;
# the total efficiency should be the maximum possible. The total efficiency equals the sum of efficiencies of all one-on-one's left.
# Given the number of people in the company n and the list of current one-on-one meetings with their efficiency values, find the best total efficiency of the reduced scheme.

# Example

# For n = 4 and meetings = [[0, 1, 3], [1, 2, 2], [3, 0, 1], [3, 2, 5]],
# the output should be
# solution(n, meetings) = 10.

# The best way to reduce meetings is to remove the 3rd (1-based) meeting from the list.



import heapq
from collections import defaultdict

def solution(n, meetings):
    # Create a graph using defaultdict
    graph = defaultdict(dict)
    for x, y, z in meetings:
        graph[x][y] = z
        graph[y][x] = z

    # Initialize visited list and priority queue
    visited = [False] * n
    priority_queue = [(0, 0)]

    total_weight = 0
    while priority_queue:
        weight, node = heapq.heappop(priority_queue)
        if not visited[node]:
            visited[node] = True
            total_weight += -weight
            for neighbor, edge_weight in graph[node].items():
                if not visited[neighbor]:
                    heapq.heappush(priority_queue, (-edge_weight, neighbor))

    return total_weight

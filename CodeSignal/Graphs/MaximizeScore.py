# Not long ago you saw an orienteering competition on TV and immediately wanted to try it yourself. You've joined an orienteering club and started preparing for the upcoming competitions.

# One day your club announced that it was going to organize its own orienteering competition and you decided to help.
# This competition will be held in a place consisting of n different locations (numbered from 0 to n - 1) connected by one-way roads. Furthermore, each road will have a number of points assigned to it: each time a participant traverse a road, this number will be added to his score. The participant who finishes with the least number of points wins. Note, that the participant can choose to continue his path to improve his score even if he reached the finish.

# The organizers of the event have already chosen where the competition will be held. The place is quite remarkable: whatever pair of locations (start, finish) is chosen, it will be impossible for any participant to gain infinitely small score. Now your task is to find the pair of locations (start, finish) with the maximum possible winning score.

# Given the number of locations n and roads between them with their respective points, return array of two elements [start, finish] such that the winning score in competition with start in location start and finish in location finish is the highest among all the other competition with different start and finish locations. If there are several possible pairs, return the lexicographically smallest one.

# Example

# For n = 7 and

# roads = [[[1, 100]],
#          [[2, -100]],
#          [[0, 0]],
#          [[0, 3], [4, 0]],
#          [[5, 1]],
#          [[3, 2]],
#          [[0, -100]]]
# the output should be
# solution(n, roads) = [1, 0].

# Example



def solution(n, roads):
    from collections import defaultdict
    from heapq import heappush, heappop

    g = defaultdict(dict)
    for i in range(n):
        for v, weight in roads[i]:
            g[i][v] = weight

    def dijkstra(head):
        queue = [(0, head)]
        d = [float('inf')] * n
        while queue:
            dis, node = heappop(queue)
            if dis < d[node]:
                d[node] = dis
                for v, weight in g[node].items():
                    if dis + weight < d[v]:
                        heappush(queue, (dis + weight, v))
        return d

    s = float('inf')
    for i in range(n):
        for v, dis in enumerate(dijkstra(i)):
            if i != v and dis < s:
                s = dis
                res = i, v
    return res

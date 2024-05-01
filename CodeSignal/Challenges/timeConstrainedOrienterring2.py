# Not long ago you saw an orienteering competition on TV and immediately wanted to try it yourself. You've joined an orienteering club and started preparing for the upcoming competitions. You liked participation so much decided to organize your very own competition, and an unusual one.

# In this race the participants should find such a path from start to finish that they will spend no more than T minutes on each road. When a participant leaves a location, the time on their stopwatch is set to T, and the countdown begins. If they can't make it to the next location in T seconds, they lose the race.

# You haven't yet chosen locations for the start and for the finish. To decide which locations to chose, for each ordered pair of locations (a, b) you'd like to calculate the minimum value of T that makes it possible to complete the race that starts at a and finishes at b.

# Given the number of locations n and one-way roads connecting them, for every start and every finish locations return the minimum possible value of T.

# Example

# For n = 3 and

# roads = [[0, 1, 100000],
#          [5, 0, 2],
#          [4, -1, 0]]
# the output should be

# solution(n, roads) = [[0, 1, 2],
#                       [4, 0, 2],
#                       [4, 4, 0]]


def solution(n, roads):
    # Copy the roads matrix to avoid modifying the original
    r = [row[:] for row in roads]

    for i in range(n):
        for j in range(n):
            for k in range(n):
                a = r[j][i]
                b = r[i][k]
                c = r[j][k]
                d = max(a, b)

                # Check if there is a path from j to i and from i to k
                if a != -1 and b != -1:
                    # If there is no direct path from j to k or the direct path is longer than the path through i
                    if c == -1 or c > d:
                        r[j][k] = d

    return r

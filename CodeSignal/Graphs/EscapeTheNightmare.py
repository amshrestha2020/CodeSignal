# Not long ago you saw an orienteering competition on TV and immediately wanted to try it yourself. You've joined an orienteering club and started preparing for the upcoming competitions.

# For the past few days you weren't able to get a good sleep because of one particular nightmare. In this nightmare you find yourself on a right star pyramid at coordinates start, and the only way to escape this nightmare is to reach the finish in the shortest possible amount of time (i.e. by the shortest path) moving along the edges of this pyramid. Tired of restless nights, you decided to put an end to it.

# Given the coordinates of start and finish located on the edges of a right start pyramid, pyramid's height h and the distance d between the center of the star at the pyramid's base and it's vertices, find the length of the shortest path from start to finish along the edges of said pyramid.

# The base of the pyramid is a regular octagram centered at (0, 0, 0) with two vertices on x axis and two vertices on y axis. The pyramid's apex is directly above (0, 0, 0) at the height h. Each pyramid's edge either belongs to the base or is connecting pyramid's apex with the base.
# It's guaranteed that both start and finish belong to the pyramid's edge.

# Here is how the given pyramid looks like:

# Pyramid

# Example

# For h = 4, d = 2, start = [-1, 0, 2], and finish = [2, 0, 0], the output should be
# solution(h, d, start, finish) = 6.7082039325.

# Example

import math

def cmp(a):
    if a < 0:
        return -1
    elif a == 0:
        return 0
    else:
        return 1

def solution(h, d, start, finish):
    h = float(h)
    x, y , i, z, t, j = start + finish
    edge = math.hypot(d,h)
    top = edge * (2 * h - i - j) / h
    bottom = (2 ** 0.5 + 2) ** 0.5 * d
    left_bot = edge * (i + j ) / h
    x,y,z,t = cmp(x),cmp(y),cmp(z),cmp(t)
    return min(top, left_bot + 2 * bottom + 2 * bottom * (x == -z and y == -t)) if x != z or y != t else edge * abs((i - j) / h)

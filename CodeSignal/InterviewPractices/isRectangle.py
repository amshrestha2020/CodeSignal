# You have four points in an array points = [[x1, y1], [x2, y2], [x3, y3], [x4, y4]]. You make a (possibly self-intersecting) 4-sided polygon by joining the adjacent points in the list and joining points[3] back to points[0]. Write a function that returns true if the shape formed by points is a rectangle, and false otherwise.

# Example

# For points = [[0, 0], [2, 0], [2, 1], [0, 1]], the output should be
# solution(points) = true.
# The shape below is a rectangle:


# For points = [[0, 0], [2, 1], [2, 0], [0, 1]], the output should be
# solution(points) = false.
# The shape below is not a rectangle:


# For points = [[0, 0], [1, 1], [0, 2], [-1, 1]], the output should be
# solution(points) = true.
# This is a square (which is a type of rectangle), even though its sides are not aligned with the axes:


# Input/Output

# [execution time limit] 4 seconds (py3)

# [memory limit] 1 GB

# [input] array.array.integer points

# The coordinates of different points in the format [[x1, y1], [x2, y2], [x3, y3], [x4, y4]].

# Guaranteed constraints:
# points.length == 4,
# points[i].length == 2,
# points[i] ≠ points[j], i ≠ j,
# -10 ≤ points[i][j] ≤ 10.

# [output] boolean

# Return true if the given points form a rectangle, otherwise return false.


def solution(points):
    def distance_squared(p1, p2):
        return (p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2
    
    def is_perpendicular(p1, p2, p3):
        dx1 = p2[0] - p1[0]
        dy1 = p2[1] - p1[1]
        dx2 = p3[0] - p2[0]
        dy2 = p3[1] - p2[1]
        return dx1 * dx2 + dy1 * dy2 == 0

    d = [distance_squared(points[i], points[(i + 1) % 4]) for i in range(4)]
    d.sort()
    return d[0] == d[1] and d[2] == d[3] and is_perpendicular(points[0], points[1], points[2]) and is_perpendicular(points[1], points[2], points[3])

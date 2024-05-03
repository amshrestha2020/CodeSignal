# Given an array of points on a 2D plane, find the maximum number of points that are visible from point (0, 0) with a viewing angle that is equal to 45 degrees.

# Example

# For

#   points = [[1, 1], [3, 1], [3, 2], [3, 3],
#             [1, 3], [2, 5], [1, 5], [-1, -1],
#             [-1, -2], [-2, -3], [-4, -4]]
# the output should be solution(points) = 6.

# This visualization shows how these 6 points can be viewed:



import math

def solution(points):
    # Calculate the angle of each point from the origin
    angles = [math.atan2(y, x) for x, y in points]
    
    # Convert angles to degrees and sort
    angles = sorted([angle * 180 / math.pi for angle in angles])
    
    # Duplicate the angles to handle the circular condition
    angles = angles + [angle + 360 for angle in angles]
    
    # Initialize variables
    max_points = 0
    j = 0
    
    # Count the maximum number of points that fall within the 45-degree viewing angle
    for i in range(len(points)):
        while angles[j] - angles[i] <= 45:
            j += 1
        max_points = max(max_points, j - i)
    
    return max_points

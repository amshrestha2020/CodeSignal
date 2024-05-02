# A rectangle with sides equal to even integers a and b is drawn on the Cartesian plane. Its center (the intersection point of its diagonals) coincides with the point (0, 0), but the sides of the rectangle are not parallel to the axes; instead, they are forming 45 degree angles with the axes.

# How many points with integer coordinates are located inside the given rectangle (including on its sides)?

# Example

# For a = 6 and b = 4, the output should be
# solution(a, b) = 23.

# The following picture illustrates the example, and the 23 points are marked green.

def solution(a, b):
    x = math.ceil(a / 2**0.5)
    y = math.ceil(b / 2**0.5)
    
    t = (x * y) + ( (x - 1) * (y - 1) )
    
    return t if t % 2 != 0 else t - 1 


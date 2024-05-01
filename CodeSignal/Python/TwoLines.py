# Implement the missing code, denoted by ellipses. You may not modify the pre-existing code.
# Consider two straight lines given as y = mx + b. You forgot what they mean but you're sure that the destiny of the universe depends on them. To save the world, you have to choose one of these lines. Here is how to make the proper choice:

# Consider all integer coordinates a for all possible values of a from l to r, inclusive.
# For each vertical x = a, find the points where this vertical intersects with line1 and line2. Denote these points as p1 and p2, respectively. If p1 and p2 don't coincide, give one point to the line which is higher in that vertical.
# Choose the line which has a larger score. Return "first" for line1, "second" for line2 and "any" if both lines have the same score.
# Example

# For line1 = [1, 2], line2 = [2, 1], l = 0, and r = 2, the output should be
# solution(line1, line2, l, r) = "any";
# For line1 = [1, 2], line2 = [2, 1], l = -1, and r = 2, the output should be
# solution(line1, line2, l, r) = "first";
# For line1 = [1, 2], line2 = [2, 1], l = 0, and r = 3, the output should be
# solution(line1, line2, l, r) = "second".

from functools import partial

def line_y(m, b, x):
    return m * x + b

def solution(line1, line2, l, r):
    line1_y = partial(line_y, *line1)
    line2_y = partial(line_y, *line2)
    balance = 0
    for x in range(l, r + 1):
        y1 = line1_y(x)
        y2 = line2_y(x)
        if y1 > y2:
            balance += 1
        elif y1 < y2:
            balance -= 1
    if balance > 0:
        return "first"
    if balance < 0:
        return "second"
    return "any"

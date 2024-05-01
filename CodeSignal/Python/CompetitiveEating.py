# Implement the missing code, denoted by ellipses. You may not modify the pre-existing code.
# The World Wide Competitive Eating tournament is going to be held in your town, and you're the one who is responsible for keeping track of time. For the great finale, a large billboard of the given width will be installed on the main square, where the time of possibly new world record will be shown.

# The track of time will be kept by a float number. It will be displayed on the board with the set precision precision with center alignment, and it is guaranteed that it will fit in the screen. Your task is to test the billboard. Given the time t, the width of the screen and the precision with which the time should be displayed, return a string that should be shown on the billboard.

# Example

# For t = 3.1415, width = 10, and precision = 2,
# the output should be

# solution(t, width, precision) = "   3

def solution(t, width, precision):
    return f"{t:.{precision}f}".center(width)

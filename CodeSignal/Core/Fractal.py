# Your task is to draw a special fractal after n iterations. The fractal consists of unit connectors '|' and '_'.

# For n = 1 the fractal looks as follows:

# _
# _|
# Now assume that you have already made N iterations and drawn the f(N) fractal. To draw the f(N + 1) fractal do the following:
# Note that every fractal has exactly two edge points which can be connected to the edge points of other fractals using the unit connectors.
# At first, take the f(N) fractal and place it in the top left corner. As the next step, put f(N) rotated by 0°, 90°, 180° or 270° in the remaining 3 quarters - top right, bottom left and bottom right - so that it is possible to connect all four of them by adding exactly 3 unit connectors between the adjacent fractal edge points.
# Note that there is always exactly one possible combination of rotations which allows to connect all 4 f(N) fractals together.

# See examples below for better understanding.

# Example

# For n = 1, the output should be
# solution(n) = [[' ', '_', ' '],       
#                [' ', '_', '|']]
# In other words, it should represent      _
# the following picture:                   _| 
# For n = 2, the output should be
# solution(n) = [[' ', '_', ' ', ' ', ' ', '_', ' '],      
#                [' ', '_', '|', ' ', '|', '_', ' '],                                  
#                ['|', ' ', ' ', '_', ' ', ' ', '|'],                                 
#                ['|', '_', '|', ' ', '|', '_', '|']]
# Or, to put it differently:  _   _
#                             _| |_
#                            |  _  |
#                            |_| |_| 
# For n = 3, the output should be
# solution(n) = [[" ", "_", " ", " ", " ", "_", "_", "_", " ", " ", " ", "_", "_", "_", " "], 
#                [" ", "_", "|", " ", "|", "_", " ", " ", "|", "_", "|", " ", " ", "_", "|"], 
#                ["|", " ", " ", "_", " ", " ", "|", " ", " ", "_", " ", " ", "|", "_", " "], 
#                ["|", "_", "|", " ", "|", "_", "|", " ", "|", " ", "|", "_", "_", "_", "|"], 
#                [" ", "_", " ", " ", " ", "_", " ", " ", "|", " ", " ", "_", "_", "_", " "], 
#                ["|", " ", "|", "_", "|", " ", "|", " ", "|", "_", "|", " ", " ", "_", "|"], 
#                ["|", "_", " ", " ", " ", "_", "|", " ", " ", "_", " ", " ", "|", "_", " "], 
#                [" ", "_", "|", " ", "|", "_", "_", "_", "|", " ", "|", "_", "_", "_", "|"]]
# The fractal looks as follows:

#                       _   ___   ___ 
#                       _| |_  |_|  _|
#                      |  _  |  _  |_ 
#                      |_| |_| | |___|
#                       _   _  |  ___ 
#                      | |_| | |_|  _|
#                      |_   _|  _  |_ 
#                       _| |___| |___|



def rotate(s):
    return list(map(lambda x: (x + 1) % 4, s))

def flip(s):
    return list(map(lambda x: 4 - x if x % 2 else x, s))

DIRECTIONS = [(0, 1), (-1, 0), (0, -1), (1, 0)]

def solution(n):
    fractal = []
    for x in range(n):
        flipped_rotated_fractal = [*flip(rotate(fractal))]
        double_rotated_fractal = [*rotate(rotate(fractal))]
        a, b, c = (3, 0, 1) if x % 2 else (0, 3, 2)
        fractal = fractal + [a] + flipped_rotated_fractal + [b] + flipped_rotated_fractal + [c] + double_rotated_fractal
    length = 2 ** n
    l = 2 * length - 1
    result = [[' ']*l for x in range(length)]
    px, py = 0, 0
    prev = -1
    for d in fractal:
        dx, dy = DIRECTIONS[d]
        if d == prev and d % 2 == 0:
            result[px][py] = '_'
        if d != 1:
            px += dx
            py += dy
        result[px][py] = '|' if d % 2 else '_'
        if dy or d == 1:
            px += dx
            py += dy
        prev = d
    return result

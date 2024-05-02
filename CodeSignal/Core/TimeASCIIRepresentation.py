# John has always liked analog clocks more than digital ones. He's been dreaming about turning his digital clock into an analog one for as long as he can remember, and now he met you, a great programmer, so his dream is about to come true.

# The screen of his digital clock is a simple 17 × 17 rectangle of pixels. It always shows four digits: the first two stand for hours and second two for minutes (John's clock uses the 24-hour format). Each digit is located in a 17 × 4 rectangle, with the leftmost column always empty, and the other three columns filled according to this pattern with the proper scaling:



# After the first two digits there is a separating column containing one symbol ':' at its center.

# Now John asks you to make his clock show time in the format similar to analog clocks. Here's how: an analog clock can be represented as a circle (the clock's borders) and two segments (the clock's hands). To show it on the 17 × 17 screen, you should light the pixels on it so that the pixel with coordinates (x, y) is enabled if and only if the minimal distance to the circle or one of the segments is less than sqrt(0.5).

# John wants you to implement the function that changes the digital representation to the analog one as described above. Given a 17 × 17 rectangle dtime representing digital time representation, return the analog representation of the same time.

# Please note that for the early prototype you have to develop, both of the clock's hands should have the same length.

# Example

# For


# dtime = [
#   ['.', '*', '*', '*', '.', '.', '*', '.', '.', '.', '*', '*', '*', '.', '*', '*', '*'],
#   ['.', '*', '.', '*', '.', '.', '*', '.', '.', '.', '.', '.', '*', '.', '*', '.', '*'],
#   ['.', '*', '.', '*', '.', '.', '*', '.', '.', '.', '.', '.', '*', '.', '*', '.', '*'],
#   ['.', '*', '.', '*', '.', '.', '*', '.', '.', '.', '.', '.', '*', '.', '*', '.', '*'],
#   ['.', '*', '.', '*', '.', '.', '*', '.', '.', '.', '.', '.', '*', '.', '*', '.', '*'],
#   ['.', '*', '.', '*', '.', '.', '*', '.', '.', '.', '.', '.', '*', '.', '*', '.', '*'],
#   ['.', '*', '.', '*', '.', '.', '*', '.', '.', '.', '.', '.', '*', '.', '*', '.', '*'],
#   ['.', '*', '.', '*', '.', '.', '*', '.', '.', '.', '.', '.', '*', '.', '*', '.', '*'],
#   ['.', '*', '.', '*', '.', '.', '*', '.', ':', '.', '*', '*', '*', '.', '*', '.', '*'],
#   ['.', '*', '.', '*', '.', '.', '*', '.', '.', '.', '.', '.', '*', '.', '*', '.', '*'],
#   ['.', '*', '.', '*', '.', '.', '*', '.', '.', '.', '.', '.', '*', '.', '*', '.', '*'],
#   ['.', '*', '.', '*', '.', '.', '*', '.', '.', '.', '.', '.', '*', '.', '*', '.', '*'],
#   ['.', '*', '.', '*', '.', '.', '*', '.', '.', '.', '.', '.', '*', '.', '*', '.', '*'],
#   ['.', '*', '.', '*', '.', '.', '*', '.', '.', '.', '.', '.', '*', '.', '*', '.', '*'],
#   ['.', '*', '.', '*', '.', '.', '*', '.', '.', '.', '.', '.', '*', '.', '*', '.', '*'],
#   ['.', '*', '.', '*', '.', '.', '*', '.', '.', '.', '.', '.', '*', '.', '*', '.', '*'],
#   ['.', '*', '*', '*', '.', '.', '*', '.', '.', '.', '*', '*', '*', '.', '*', '*', '*']
# ]
# the output should be


# solution(dtime) = [
#   ['.', '.', '.', '.', '*', '*', '*', '*', '*', '*', '*', '*', '*', '.', '.', '.', '.'],
#   ['.', '.', '.', '*', '*', '.', '.', '.', '.', '.', '.', '.', '*', '*', '.', '.', '.'],
#   ['.', '.', '*', '*', '.', '.', '.', '.', '.', '.', '.', '.', '.', '*', '*', '.', '.'],
#   ['.', '*', '*', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '*', '*', '*', '.'],
#   ['*', '*', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '*', '.', '.', '*', '*'],
#   ['*', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '*', '.', '.', '.', '.', '*'],
#   ['*', '.', '.', '.', '.', '.', '.', '.', '.', '.', '*', '.', '.', '.', '.', '.', '*'],
#   ['*', '.', '.', '.', '.', '.', '.', '.', '.', '*', '.', '.', '.', '.', '.', '.', '*'],
#   ['*', '.', '.', '.', '.', '.', '.', '.', '*', '.', '.', '.', '.', '.', '.', '.', '*'],
#   ['*', '.', '.', '.', '.', '.', '.', '.', '*', '.', '.', '.', '.', '.', '.', '.', '*'],
#   ['*', '.', '.', '.', '.', '.', '.', '.', '*', '.', '.', '.', '.', '.', '.', '.', '*'],
#   ['*', '.', '.', '.', '.', '.', '.', '.', '*', '.', '.', '.', '.', '.', '.', '.', '*'],
#   ['*', '*', '.', '.', '.', '.', '.', '.', '*', '.', '.', '.', '.', '.', '.', '*', '*'],
#   ['.', '*', '*', '.', '.', '.', '.', '.', '*', '.', '.', '.', '.', '.', '*', '*', '.'],
#   ['.', '.', '*', '*', '.', '.', '.', '.', '*', '.', '.', '.', '.', '*', '*', '.', '.'],
#   ['.', '.', '.', '*', '*', '.', '.', '.', '*', '.', '.', '.', '*', '*', '.', '.', '.'],
#   ['.', '.', '.', '.', '*', '*', '*', '*', '*', '*', '*', '*', '*', '.', '.', '.', '.']
# ]
# (Enabled pixels are painted red to make them more visible).

# Here is the geometrical representation of an analog clock showing time 01:30. Enabled pixel are painted red.


import math

def solution(dtime):
    digit_patterns = ["***.***", "*..*..*", "*.***.*", "*.**.**", ".***.*.", "**.*.**", "**.****", "*.*..*.", "*******", "****.**"]
    digits = [digit_patterns.index("".join(dtime[j][i+k] for j, k in [[0, 1], [4, 0], [4, 2], [8, 1], [12, 0], [12, 2], [16, 1]])) for i in [1, 5, 10, 14]]
    return [["*" if abs(math.sqrt((i-8)**2+(j-8)**2)-8.5) < math.sqrt(0.5) or math.sqrt((i-8)**2+(j-8)**2) < 8.5 and any([(j-8)*math.sin(a*2*math.pi)+(8-i)*math.cos(a*2*math.pi) >= 0 and abs((j-8)*math.cos(a*2*math.pi)-(8-i)*math.sin(a*2*math.pi)) < math.sqrt(0.5)-1e-9 for a in [(10*digits[0]+digits[1]+(10*digits[2]+digits[3])/60)/12, (10*digits[2]+digits[3])/60]]) else "." for j in range(17)] for i in range(17)]


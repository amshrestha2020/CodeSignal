# You are given a vertical box divided into equal columns. Someone dropped several stones from its top through the columns. Stones are falling straight down at a constant speed (equal for all stones) while possible (i.e. while they haven't reached the ground or they are not blocked by another motionless stone). Given the state of the box at some moment in time, find out which columns become motionless first.

# Example

# For

# rows = ["#..##",
#         ".##.#",
#         ".#.##",
#         "....."]
# the output should be solution(rows) = [1, 4].

# Check out the image below for better understanding:

def solution(rows):
    result = []
    min_steps_required = float('inf')

    for col in range(len(rows[0])):
        row = len(rows) - 1
        cur_min_steps_required = 0
        prev_cur_min_steps_required = 0

        while row >= 0:
            while row >= 0 and rows[row][col] == "#":
                row -= 1
            while row >= 0 and rows[row][col] == ".":
                row -= 1
                cur_min_steps_required += 1
            if row >= 0:
                prev_cur_min_steps_required = cur_min_steps_required
            else:
                while result and min_steps_required > prev_cur_min_steps_required:
                    result.pop()
                if min_steps_required >= prev_cur_min_steps_required:
                    result.append(col)
                    min_steps_required = prev_cur_min_steps_required

    return result

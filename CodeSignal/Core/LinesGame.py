# Let's remember the '90s and play an old-school Lines game with the following rules.

# The game starts with a 9 × 9 field with several colored balls placed on its cells (there are 7 possible colors but not all colors have to be present initially). The player can move one ball per turn, and they may only move a ball if there is a clear path between the current position of the chosen ball and the desired destination. Clear paths are formed by neighboring empty cells. Two cells are neighboring if they have a common side. The goal is to remove balls by forming lines (horizontal, vertical or diagonal) of at least five balls of the same color. If the player manages to form one or more such lines, the move is called successful, and the balls in those lines disappear. Otherwise, the move is called unsuccessful, and three more balls appear on the field.

# You are given the game logs, and your task is to calculate the player's final score. Here's the information you have:

# The field state at the initial moment;
# The clicks the user has made. Note that a click does not necessarily result in a move:
# If the user clicks a ball and then another, the first click is ignored;
# If two consecutive clicks result in an incorrect move, they are ignored;
# After each unsuccessful move three more balls appear:
# newBalls contains the balls' colors;
# newBallsCoordinates contains their coordinates;
# Note that after the balls appear, new lines may form;
# Whenever new lines appear, they are removed and the player receives A + B - 1 points, where:
# A is the number of lines of at least five balls;
# B is the total number of balls in those lines;
# Possible ball colors are red, blue, orange, violet, green, yellow and cyan, which are represented in logs by
# "R", "B", "O", "V", "G", "Y" and "C" respectively.
# Example

# For

# field = [['.', 'G', '.', '.', '.', '.', '.', '.', '.'],
#          ['.', '.', '.', '.', '.', '.', '.', 'V', '.'],
#          ['.', 'O', '.', '.', 'O', '.', '.', '.', '.'],
#          ['.', '.', '.', '.', 'O', '.', '.', '.', '.'],
#          ['.', '.', '.', '.', '.', '.', '.', '.', 'O'],
#          ['.', '.', '.', '.', 'O', '.', '.', '.', '.'],
#          ['.', '.', '.', '.', '.', '.', '.', '.', '.'],
#          ['R', '.', '.', '.', '.', '.', '.', 'B', 'R'],
#          ['.', '.', 'C', '.', '.', '.', '.', 'Y', 'O']]
# clicks = [[4, 8], [2, 1], [4, 4], [6, 4], [4, 8], [1, 2], [1, 4], [4, 8], [6, 4]],
# newBalls = ['R', 'V', 'C', 'G', 'Y', 'O'], and
# newBallsCoordinates = [[1, 2], [8, 5], [8, 6], [1, 1], [1, 8], [7, 4]], the output should be
# solution(field, clicks, newBalls, newBallsCoordinates) = 6.

# The only correct moves were:

# Orange ball moved from [2, 1] to [4, 4];
# Red ball moved from [1, 2] to [1, 4];
# Orange ball moved from [4, 8] to [6, 4]
# After the third move a vertical line with 6 orange balls appears, so it is removed and the player receives 1 + 6 - 1 = 6 points.



# For

# field = [['.', '.', '.', '.', '.', '.', '.', '.', '.'],
#          ['.', '.', '.', '.', '.', '.', '.', '.', '.'],
#          ['.', '.', 'O', '.', 'O', '.', 'O', '.', '.'],
#          ['.', '.', '.', 'O', 'O', 'O', '.', '.', '.'],
#          ['.', '.', '.', '.', '.', '.', '.', '.', 'O'],
#          ['.', '.', '.', 'O', 'O', 'O', '.', '.', '.'],
#          ['.', '.', 'O', '.', 'O', '.', 'O', '.', '.'],
#          ['.', '.', '.', '.', '.', '.', '.', '.', '.'],
#          ['.', '.', '.', '.', '.', '.', '.', '.', '.']]
# clicks = [[4, 8], [4, 4]],
# newBalls = [], and
# newBallsCoordinates = [], the output should be
# solution(field, clicks, newBalls, newBallsCoordinates) = 17.

# After the move there will be three lines with exactly 5 balls of the same color, so the answer is 3 + (5 + 5 + 5) - 1 = 17.

def solution(field, clicks, newBalls, newBallsCoordinates):
    def dfs(start_x, start_y, end_x, end_y):
        queue = [(start_x, start_y)]
        visited = set()
        while queue:
            current_x, current_y = queue.pop()
            for i, j in {(current_x, current_y + 1), (current_x, current_y - 1), (current_x + 1, current_y), (current_x - 1, current_y)} - visited:
                if 0 <= i < len(field) and 0 <= j < len(field[0]) and field[i][j] == '.':
                    if (i, j) == (end_x, end_y):
                        return True
                    queue.append((i, j))
                    visited.add((i, j))
        return False

    def calculate_score_and_clear():
        clear_set = set()

        for x in range(len(field)):
            for y in range(len(field[0])):
                color = field[x][y]
                if color == ".":
                    continue
                sub_scores = [[(x, y)] for _ in range(4)]
                directions = [[0, 1], [1, 1], [1, 0], [1, -1]]
                for _ in range(2):
                    keep_checking = [True, True, True, True]
                    multiplier = 1
                    while any(keep_checking):
                        for i, (dx, dy) in enumerate(directions):
                            if not keep_checking[i]:
                                continue
                            next_x = x + multiplier * dx
                            next_y = y + multiplier * dy
                            if 0 <= next_x < len(field) and 0 <= next_y < len(field[0]) and field[next_x][next_y] == color:
                                sub_scores[i] += [(next_x, next_y)]
                            else:
                                keep_checking[i] = False
                        multiplier += 1
                    # flip directions and repeat:
                    directions = [[-a, -b] for a, b in directions]

                for z in sub_scores:
                    if len(z) >= 5:
                        z = sorted(z)
                        clear_set.add(tuple(z))

        a = len(clear_set)
        b = sum([len(l) for l in clear_set])
        flat_clears = {p for t in clear_set for p in t}
        # clear long lines:
        for (cx, cy) in flat_clears:
            field[cx][cy] = "."

        return max(0, a + b - 1)

    i = 0  # current index of newBalls
    selected = False
    start_x, start_y = 0, 0
    final_score = 0

    for x, y in clicks:
        if field[x][y] != '.':  # clicked a ball
            selected = True
            start_x, start_y = x, y
        else:
            if selected and dfs(start_x, start_y, x, y):
                field[start_x][start_y], field[x][y] = '.', field[start_x][start_y]

                # check for completed lines:
                score = calculate_score_and_clear()

                if score == 0:  # unsuccessful, place 3 new balls
                    for z in range(3):
                        ax, ay = newBallsCoordinates[i + z]
                        color = newBalls[i + z]
                        field[ax][ay] = color
                    i += 3
                    # check score once more:
                    final_score += calculate_score_and_clear()
                else:  # success
                    final_score += score

            selected = False

    return final_score

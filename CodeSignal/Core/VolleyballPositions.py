# You are watching a volleyball tournament, but you missed the beginning of the very first game of your favorite team. Now you're curious about how the coach arranged the players on the field at the start of the game.

# The team you favor plays in the following formation:

# 0 3 0
# 4 0 2
# 0 6 0
# 5 0 1
# where positive numbers represent positions occupied by players. After the team gains the serve, its members rotate one position in a clockwise direction, so the player in position 2 moves to position 1, the player in position 3 moves to position 2, and so on, with the player in position 1 moving to position 6.

# Here's how the players change their positions:



# Given the current formation of the team and the number of times k it gained the serve, find the initial position of each player in it.

# Example

# For

# formation = [["empty",   "Player5", "empty"],
#              ["Player4", "empty",   "Player2"],
#              ["empty",   "Player3", "empty"],
#              ["Player6", "empty",   "Player1"]]
# and k = 2, the output should be

# solution(formation, k) = [
#     ["empty",   "Player1", "empty"],
#     ["Player2", "empty",   "Player3"],
#     ["empty",   "Player4", "empty"],
#     ["Player5", "empty",   "Player6"]
# ]
# For

# formation = [["empty", "Alice", "empty"],
#              ["Bob",   "empty", "Charlie"],
#              ["empty", "Dave",  "empty"],
#              ["Eve",   "empty", "Frank"]]
# and k = 6, the output should be

# solution(formation, k) = [
#     ["empty", "Alice", "empty"],
#     ["Bob",   "empty", "Charlie"],
#     ["empty", "Dave",  "empty"],
#     ["Eve",   "empty", "Frank"]
# ]

def solution(formation, k):
    k %= 6
    if k == 0:
        return formation

    locations = [
        [3, 2],
        [1, 2],
        [0, 1],
        [1, 0],
        [3, 0],
        [2, 1],
    ]
    names = [formation[row][col] for row, col in locations]

    for index, _ in enumerate(locations):
        nextRow, nextCol = locations[(index + k) % 6]
        formation[nextRow][nextCol] = names[index]

    return formation

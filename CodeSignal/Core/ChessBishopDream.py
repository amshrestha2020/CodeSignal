# In ChessLand there is a small but proud chess bishop with a recurring dream. In the dream the bishop finds itself on an n × m chessboard with mirrors along each edge, and it is not a bishop but a ray of light. This ray of light moves only along diagonals (the bishop can't imagine any other types of moves even in its dreams), it never stops, and once it reaches an edge or a corner of the chessboard it reflects from it and moves on.

# Given the initial position and the direction of the ray, find its position after k steps where a step means either moving from one cell to the neighboring one or reflecting from a corner of the board.

# Example

# For boardSize = [3, 7], initPosition = [1, 2],
# initDirection = [-1, 1], and k = 13, the output should be
# solution(boardSize, initPosition, initDirection, k) = [0, 1].

# Here is the bishop's path:

# [1, 2] -> [0, 3] -(reflection from the top edge)-> [0, 4] -> 
# [1, 5] -> [2, 6] -(reflection from the bottom right corner)-> [2, 6] ->
# [1, 5] -> [0, 4] -(reflection from the top edge)-> [0, 3] ->
# [1, 2] -> [2, 1] -(reflection from the bottom edge)-> [2, 0] -(reflection from the left edge)->
# [1, 0] -> [0, 1]


def solution(boardSize, initPosition, initDirection, k):
    pointer = 0
    points = set()

    while pointer < k:
        point = get_position_point(initPosition, initDirection)

        if point in points:
            k %= pointer
            pointer = 0
            break

        pointer += 1
        points.add(point)
        get_next_position(boardSize, initPosition, initDirection)

    while pointer < k:
        pointer += 1
        get_next_position(boardSize, initPosition, initDirection)

    return initPosition

def get_position_point(initPosition, initDirection):
    point = 0
    point += initPosition[0]
    point += initPosition[1] * 100
    point += initDirection[0] * 10000
    point += initDirection[1] * 1000000
    return point

def get_next_position(boardSize, position, direction):
    nextRow = position[0] + direction[0]
    nextCol = position[1] + direction[1]
    isRowValid = 0 <= nextRow < boardSize[0]
    isColValid = 0 <= nextCol < boardSize[1]
    if isRowValid:
        position[0] = nextRow
    else:
        direction[0] *= -1
    if isColValid:
        position[1] = nextCol
    else:
        direction[1] *= -1

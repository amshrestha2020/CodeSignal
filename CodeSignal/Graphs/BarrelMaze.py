# After long years of sharpening your programming skills and honing your physique you finally made it: as a member of the ProProgrammers team you've entered Fort Boyard!

# Your team has successfully completed several challenges so far, and one of your teammates is ready to face the next one. In this challenge the player must move a barrel from one end of an n × m maze to the other where the key is locked in a vice. A tool that releases the key is connected to the barrel. The maze consists of n · m - 3 boxes, and these boxes and the barrel should be moved so that the key can be freed. The boxes and the barrel are really heavy, so you decided to help your teammate to plan his moves.

# Given the size of the maze and boxes positions, find the minimum number of moves required to complete the challenge.

# Example

# For n = 3, m = 3, and
# boxes = [[0, 2], [2, 2], [1, 0], [2, 0], [1, 1], [2, 1]],
# the output should be
# solution(n, m, boxes) = 8.

# This is how one of the possible solutions looks like:


from collections import deque

def solution(n, m, boxes):
    # Create a grid to represent the maze
    grid = [[{(i, j+1), (i, j-1), (i+1, j), (i-1, j)} for j in range(m)] for i in range(n)]
    # Trim top and bottom
    for col in range(m):
        grid[0][col].remove((-1, col))
        grid[n-1][col].remove((n, col))
    # Trim sides
    for row in range(n):
        grid[row][0].remove((row, -1))
        grid[row][m-1].remove((row, m))

    # Create the initial state
    empty_spaces = {(i, j) for i in range(n) for j in range(m)}
    empty_spaces.remove((0, 0))
    for [row, col] in boxes:
        empty_spaces.remove((row, col))
    initial_state = (frozenset(empty_spaces), (0, 0))

    # Function to generate next states
    def next_states(state):
        next_states = []
        empties, barrel = state
        empties = set(empties)  # Unfreeze so that it can be modified
        for (row, col) in empties:  # For all (both) empty spaces
            for (nr, nc) in grid[row][col]:  # For each of their neighbors
                if (nr, nc) in empties:  # Skip if there's no box there
                    continue
                next_empties = empties.copy()  # Copy to avoid modifying the original
                next_empties.remove((row, col))
                next_empties.add((nr, nc))
                next_barrel = barrel
                if (nr, nc) == barrel:
                    next_barrel = (row, col)
                next_states.append((frozenset(next_empties), next_barrel))
        return next_states

    # Depth-first search
    states, target = {initial_state}, (n-1, m-1)
    frontier, horizon, moves = {initial_state}, set(), 0
    while frontier:
        moves += 1
        for state in frontier:
            for next_state in next_states(state):
                if next_state not in states:
                    if next_state[1] == target:
                        return moves
                    states.add(next_state)
                    horizon.add(next_state)
        frontier, horizon = horizon, set()

    return -1

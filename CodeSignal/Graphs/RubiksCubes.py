# After long years of sharpening your programming skills and honing your physique you finally made it: as a member of the ProProgrammers team you've entered Fort Boyard!

# Unfortunately it looks like something went horribly wrong: although you collected the treasure of the Fort, you cannot get out of there! You asked a crazed Professor (inhabitant of the Fort) to help you out, and he showed you the gates that lead to the exit. It turned out that opening the gates is a challenge itself, and you will be allowed to leave the Fort only if you manage to complete it from the first try. Moreover, the Master Of The Fort is after you because of your outstanding performance, so you don't have that much time.

# Two of your teammates are given Rubik's Cubes, one cube for each player. The gates that will open only when the cubes have the same configuration, and only if this configuration is obtained in the minimum possible number of moves. Each move each of the players is allowed to rotate one of the layers of their cube. There are two additional conditions that should be met. Firstly, it's not possible to rotate the cubes, since it will open the tigers' cages in the room where the other teammates are waiting. Secondly, each move a layer can be rotated only 90°.

# Given initial cubes configurations, return the minimum number of moves required to obtain the same configuration on both cubes. The time is short, so you can make only 2 moves.

# Example

# For

# firstCube = [[0, 0, 0, 0], [1, 1, 1, 1], [2, 2, 2, 2], 
#              [3, 3, 3, 3], [4, 4, 4, 4], [5, 5, 5, 5]]
# and

# secondCube = [[5, 0, 3, 0], [1, 4, 1, 2], [5, 5, 2, 2],
#               [3, 4, 3, 4], [0, 2, 0, 4], [3, 1, 5, 1]]
# the output should be
# solution(firstCube, secondCube) = 1.

# Here is what the first cube looks like:



# And here is what the second cube looks like:



# If the first teammate rotates the upper layer to the left and the second teammate rotates the left layer backwards, both of them will get the following configuration:


import numpy as np

def solution(firstCube, secondCube):
    # Flatten everything
    first = np.array(firstCube).flatten()
    second = np.array(secondCube).flatten()

    # Define corners - (face, square) going clockwise
    corners = np.apply_along_axis(lambda x: x[0]*4+x[1], 2, np.array([
        ((0, 0), (3, 0), (5, 1)), ((0, 1), (5, 0), (2, 1)),
        ((0, 2), (4, 0), (3, 1)), ((0, 3), (2, 0), (4, 1)),
        ((1, 0), (2, 3), (5, 2)), ((1, 1), (5, 3), (3, 2)),
        ((1, 2), (4, 3), (2, 2)), ((1, 3), (3, 3), (4, 2)),
    ]))
    
    # Define vertices (map from face piece to the other parts of the vertex)
    vertices = [x[1:] for x in sorted(np.vstack([np.roll(corners,i,axis=1) for i in range(3)]).tolist())]

    # Build permutation groups using vertices
    groups = [
        [face, np.array([vertices[x] for x in face]).flatten()]
        for face in np.arange(24).reshape((6, 4))[:, [0, 1, 3, 2]]
    ]

    # Build moves from permutation groups
    moves = []
    for group in groups:
        for i in [1, -1]:
            x = np.arange(24)
            x[group[0]] = x[np.roll(group[0], i)]
            x[group[1]] = x[np.roll(group[1], 2 * i)]
            moves.append(x)

    configs_first = set([tuple(first)])
    configs_second = set([tuple(second)])

    if np.array_equal(first, second):
        return 0
    for i in [1, 2]:
        for c in list(configs_first):
            for m in moves:
                configs_first.add(tuple(np.array(c)[m]))
        for c in list(configs_second):
            for m in moves:
                configs_second.add(tuple(np.array(c)[m]))
        if configs_first.intersection(configs_second):
            return i

    return -1

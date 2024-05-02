# You've mastered the Rubik's Cube and got bored solving it, so now you are looking for a new challenge. One puzzle similar to the Rubik's Cube caught your attention. It's called a Pyraminx puzzle, and is a triangular pyramid-shaped puzzle. The parts are arranged in a pyramidal pattern on each side, while the layers can be rotated with respect to each vertex, and the individual tips can be rotated as well. There are 4 faces on the Pyraminx. The puzzle should be held so that one face faces you and one face faces down, as in the image below. The four corners are then labeled U (for up), R (for right), L (for left), and B (for back). The front face thus contains the U, R, and L corners.



# Let's write down all possible moves for vertex U in the following notation:

# U - 120° counterclockwise turn of topmost tip (assuming that we're looking at the pyraminx from the top, and vertex U is the topmost);
# U' - clockwise turn for the same tip;
# u - 120° counterclockwise turn of two upper layer;
# u' - clockwise turn for the same layers.


# For other vertices the moves can be described similarly:



# The first puzzle you bought wasn't assembled, so you get your professional pyraminx solver friend to assemble it. He does, and you wrote down all his moves notated as described above. Now the puzzle's faces have colors faceColors[0] (front face), faceColors[1] (bottom face), faceColors[2] (left face), faceColors[3] (right face). You want to know the initial state of the puzzle to repeat your friend's moves and see how he solved it.

# Example

# For faceColors = ['R', 'G', 'Y', 'O'] and moves = ["B", "b'", "u'", "R"], the output should be

# solution(faceColors, moves) = [['Y', 'Y', 'Y', 'Y', 'R', 'R', 'R', 'R', 'G'],
#                                ['G', 'R', 'O', 'O', 'O', 'G', 'G', 'G', 'G'],
#                                ['Y', 'O', 'Y', 'G', 'O', 'O', 'G', 'G', 'Y'],
#                                ['R', 'O', 'O', 'R', 'O', 'Y', 'Y', 'R', 'R']]
# Let's repeat the friend's steps in reverse order:

# Final state:



# Before the last move:



# One more move before that:



# And one more:



# Finally, the initial state:



def triswap(a, b, c, direction):
    d = a
    if direction:
        a, b, c = b, c, d
    else:
        a, b, c = c, b, d
    return a, b, c

def swapFaces(faces, A, a, B, b, C, c, direction):
    faces[A][a], faces[B][b], faces[C][c] = triswap(faces[A][a], faces[B][b], faces[C][c], direction)

def solution(faceColors, moves):
    singleRotationSequence  = [0,4,8]
    doubleRotationSequences = [singleRotationSequence,[1,6,3],[2,5,7],[3,1,6]]
    rotationVertices = {"R":[3,1,0],"B":[1,3,2],"L":[2,0,1],"U":[0,2,3]}
    
    moves = moves[::-1]
    pyraminx = [[x]*9 for x in faceColors]
    for move in moves:
        primaryVertices = rotationVertices[move[0].upper()]
        direction = 2*(len(move)-1)-1 # -1 if backwards, 1 otherwise
        primaryVertices = primaryVertices[::direction]
        x1,y1,z1 = primaryVertices
        single = move[0].upper() == move[0]
        if single:
            sequences = [singleRotationSequence]
        else:
            sequences = doubleRotationSequences
        for sequence in sequences:
            x2,y2,z2 = sequence[::direction]
            pyraminx[x1][x2],pyraminx[y1][y2],pyraminx[z1][z2] = pyraminx[y1][y2],pyraminx[z1][z2],pyraminx[x1][x2]
        print(move)
        [print(line) for line in pyraminx]
    return pyraminx

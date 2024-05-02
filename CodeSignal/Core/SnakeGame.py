# Your task is to imitate a turn-based variation of the popular "Snake" game.



# You are given the initial configuration of the board and a list of commands which the snake follows one-by-one. The game ends if one of the following happens:

# the snake tries to eat its tail;
# the snake tries to move out of the board;
# it executes all the given commands.
# Output the board configuration after the game ends.

# Example

# For
# gameBoard = [['.', '.', '.', '.'],
#              ['.', '.', '<', '*'],
#              ['.', '.', '.', '*']]
# and commands = "FFFFFRFFRRLLF", the output should be

# solution(gameBoard, commands) = [['.', '.', '.', '.'],
#                                  ['X', 'X', 'X', '.'],
#                                  ['.', '.', '.', '.']]
# For
# gameBoard = [['.', '.', '^', '.', '.'],
#              ['.', '.', '*', '*', '.'],
#              ['.', '.', '.', '*', '*']]
# and commands = "RFRF", the output should be

# solution(gameBoard, commands) = [['.', '.', 'X', 'X', '.'],
#                                  ['.', '.', 'X', 'X', '.'],
#                                  ['.', '.', '.', 'X', '.']]
# For
# gameBoard = [['.', '.', '*', '>', '.'],
#              ['.', '*', '*', '.', '.'],
#              ['.', '.', '.', '.', '.']]
# and commands = "FRFFRFFRFLFF", the output should be

# solution(gameBoard, commands) = [['.', '.', '.', '.', '.'],
#                                  ['<', '*', '*', '.', '.'],
#                                  ['.', '.', '*', '.', '.']]

import numpy

def solution(g, commands):
    g = numpy.r_[g]
    direction = {'^': [-1, 0], '>': [0, 1], 'v': [1, 0], '<': [0, -1]}
    left, right, row, col  = '^<v>^', '^>v<^', len(g), len(g[0])
    res= numpy.full((row, col),'.')
    valid = lambda x,y : 0 <= x < row and 0 <=y <col
    def dfs(x,y):
        stack, seen = [(x,y)], {(x,y)}
        while stack:
            x,y = stack.pop(0)
            snake.append([x,y])
            for i,j in (0,1),(1,0),(-1,0),(0,-1):
                if valid(x+i, y+j) and not (x+i, y+j) in seen and g[x+i,y+j] == '*':
                    seen.add((x+i, y+j))
                    stack.append([x+i, y+j])
    snake = []
    for i in range(row):
        for j in range(col):
            if g[i,j] in '^>v<':
                curr, head = [i, j], g[i,j]
                dfs(i,j)
    for d in commands:
        if d == 'F':
            k = snake.pop()
            i, j = direction[head]
            curr = [curr[0] +i, curr[1] +j]
            if valid(*curr) and not curr in snake : snake.insert(0,curr)
            else:
                for x,y in snake + [k] : res[x,y] = 'X'
                return res
        else:
            head = left[left.index(head)+1] if d == 'L' else right[right.index(head)+1]
    i, j = snake[0] ; res[i, j] = head 
    for x, y in snake[1:]:
        res[x, y] = '*'
    return res
        
            
   
    
    


# Little Ratiorg was tired of being bullied by other bots and mighty CodeFighters, so he joined the Ninja Bots Training camp. Any bot that manages to solve all the challenges becomes an ultimate master of algorithms, and that is exactly what Ratiorg wants.

# It's been several weeks, and Ratiorg is starting to boast about his newly obtained skills, which infuriates one of his fellow trainees. The angry bot decided to challenge Ratiorg to a Mobius Conquer battle to find out who's the strongest once and for all.

# In the Mobius Conquer battle the players fight for positions on a Möbius strip, created from a rectangular field by giving it a half-twist, and then joining the ends of the strip along its height to form a loop. Both sides of the field are divided into cells, some of which are marked as impassable (note that player positions are not considered impassable). A player is said to control a cell if the cell is closer to him in terms of shortest paths on the strip.

# The Mobius Conquer battle is almost over: ratiorg and his enemy have both reached their final positions. The only thing to do now is to determine the winner. Given the coordinates of both players, coordinates of the impassableCells and the size of the field, calculate the number of cells controlled by each player.

# Example

# For field = [4, 3], ratiorg = [0, 0, 0], enemy = [1, 3, 2], and

# impassableCells = [[0, 0, 1], [0, 1, 1], [0, 2, 1], [0, 2, 2],
#                    [1, 1, 0], [1, 2, 1], [1, 3, 0]]
# the output should be
# solution(field, ratiorg, enemy, impassableCells) = [7, 6].

# Here's what each side of the field looks like:



# And here's what the Möbius strip obtained from it looks like:



from collections import defaultdict, deque
import numpy as np

def BFS(graph, passable, distance, root):
    queue = deque([root])
    while queue:
        vertex = queue.popleft()
        for neighbor in graph[vertex]:
            if passable[neighbor] and (distance[neighbor] == -1):
                queue.append(neighbor)
                distance[neighbor] = distance[vertex] + 1 
    return distance

def solution(field, ratiorg, enemy, impassable):
    graph = defaultdict(list)
    m, n = field

    for k in range(2):
        for i in range(m):
            for j in range(n):
                if i != 0:
                    graph[(k,i,j)].append((k,i-1,j))
                if i != m-1:
                    graph[(k,i,j)].append((k,i+1,j))
                graph[(k,i,j)].append(((k-(j==0))%2,i,(j-1)%n))
                graph[(k,i,j)].append(((k+(j==(n-1)))%2,i,(j+1)%n))

    passable = {cell: 1 for cell in graph}
    for cell in impassable:
        passable[tuple(cell)] = 0 

    distance = {cell: -1 for cell in graph} 
    distance[tuple(ratiorg)] = 0
    distance0 = BFS(graph, passable, distance, tuple(ratiorg))

    distance = {cell: -1 for cell in graph} 
    distance[tuple(enemy)] = 0
    distance1 = BFS(graph, passable, distance, tuple(enemy))

    x = sum([distance0[(k,i,j)]<distance1[(k,i,j)] for k in range(2) for i in range(m) for j in range(n)]) 
    y = sum([distance0[(k,i,j)]>distance1[(k,i,j)] for k in range(2) for i in range(m) for j in range(n)]) 

    return [x,y]

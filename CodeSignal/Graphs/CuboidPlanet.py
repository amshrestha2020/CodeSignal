# Little Ratiorg was so tired of being bullied by other bots and mighty CodeFighters that he decided to join the Ninja Bots Training camp. It is known that any bot that manages to solve all the challenges becomes an ultimate master of algorithms, and that is exactly what Ratiorg is aiming at.

# Ratiorg has become so cool that the authorities decided to send him on a special mission to the remote cuboid planet of size a × b × c, not yet inhabited by bots. In order to prepare for the mission, Ratiorg has to understand the properties of the planet by training on its net here, on Earth. Here's how the planet and the net on which the bot is going to prepare for the mission look like:

 

# The net is divided into 6 areas, with each area representing one of the planet's surfaces. Each of the areas is divided into a grid with cells of size 1 × 1, with some of the cells being impassable. The coordinates of each cell can be represented in the format (area, row, column), where area stands for the area number shown in the net image above, and (row, column) stands for 0-based cell's position in this area. It is possible to move between two cells if they share a common side.

# Ratiorg would like understand how close the net he's going to train on is to the conditions of the planet. In order to do this, he would like to calculate the difference between the numbers of pairs of cells that are reachable from one another on a cuboid and the number of pairs of cells that are reachable from one another on a net (note that only pairs of different cells should be counted, and the order of cells in a pair doesn't matter, i.e. (a, b) is the same pair as (b, a)).

# Given the dimensions of the cuboid and the impassableCells, calculate the value Ratiorg is interested in.

# Example

# For cuboid = [1, 2, 3] and
# impassableCells = [[1, 0, 0], [3, 0, 1], [3, 2, 0], [4, 0, 1], [5, 1, 0]],
# the output should be
# solution(cuboid, impassableCells) = 106.

# On a cuboid, all cells but the impassable ones are reachable from one another, so the total number of reachable pairs equals 17 * 16 / 2 = 136.

# Here's how the net of this cuboid looks like:



# There are four areas in which all cells are connected. Thus, the number of pairs of cells that are reachable from one another is
# 3 * 2 / 2 + 4 * 3 / 2 + 4 * 3 / 2 + 6 * 5 / 2 = 30.

# Thus, the answer is 136 - 30 = 106.


class Cuboid(object):
    
    def __init__(self, cuboid, impassableCells):
        self.a, self.b, self.c = cuboid
        self.impassableCells = set(map(tuple, impassableCells))
    
    def cells(self):
        for r in range(self.a):
            for c in range(self.c):
                yield (0, r, c)
        
        for r in range(self.a):
            for c in range(self.b):
                yield (1, r, c)
    
        for r in range(self.a):
            for c in range(self.c):
                yield (2, r, c)
    
        for r in range(self.c):
            for c in range(self.b):
                yield (3, r, c)
    
        for r in range(self.a):
            for c in range(self.b):
                yield (4, r, c)
    
        for r in range(self.c):
            for c in range(self.b):
                yield (5, r, c)
    
    def moves(self, r, c):
        for i, j in ((0, -1), (-1, 0), (0, 1), (1, 0)):
            yield (r + i, c + j)

    def connected(self):
        from collections import deque
        components = []
        visited = set()
        
        for start in self.cells():
            if start in visited or start in self.impassableCells:
                continue
            
            queue = deque([start])
            component = set()
            
            while queue:
                u = queue.popleft()

                if not u in visited:
                    visited.add(u)
                    component.add(u)
                    
                    for v in self.adjacent(*u):
                        if not v in visited and not v in self.impassableCells:
                            queue.append(v)
            
            if component:
                components.append(component)
        
        return components

class CuboidNet(Cuboid):
    def adjacent(self, area, r, c):
        for u, v in self.moves(r, c):

            if area == 0:
                if u >= 0 and u < self.a and v >= 0 and v < self.c:
                    yield (0, u, v)
                elif u >= 0 and u < self.a and v == self.c:
                    yield (1, u, 0)
            
            elif area == 1:
                if u >= 0 and u < self.a and v >= 0 and v < self.b:
                    yield (1, u, v)
                elif u >= 0 and u < self.a and v == -1:
                    yield (0, u, self.c - 1)
                elif u >= 0 and u < self.a and v == self.b:
                    yield (2, u, 0)  
                elif u == self.a and v >= 0 and v < self.b:
                    yield (3, 0, v)

            elif area == 2:
                if u >= 0 and u < self.a and v >= 0 and v < self.c:
                    yield (2, u, v)
                elif u >= 0 and u < self.a and v == -1:
                    yield (1, u, self.b - 1)
            
            elif area == 3:
                if u >= 0 and u < self.c and v >= 0 and v < self.b:
                    yield (3, u, v)
                elif u == -1 and v >= 0 and v < self.b:
                    yield (1, self.a - 1, v)
                elif u == self.c and v >= 0 and v < self.b:
                    yield (4, 0, v)
            
            elif area == 4:
                if u >= 0 and u < self.a and v >= 0 and v < self.b:
                    yield (4, u, v)
                elif u == -1 and v >= 0 and v < self.b:
                    yield (3, self.c - 1, v)
                elif u == self.a and v >= 0 and v < self.b:
                    yield (5, 0, v)
            
            elif area == 5:
                if u >= 0 and u < self.c and v >= 0 and v < self.b:
                    yield(5, u, v)
                elif u == -1 and v >= 0 and v < self.b:
                    yield(4, self.a - 1, v)


class CuboidPlanet(Cuboid):
    
    def adjacent(self, area, r, c):
        for u, v in self.moves(r, c):

            if area == 0:
                if u >= 0 and u < self.a and v >= 0 and v < self.c:
                    yield (0, u, v)
                elif u == -1 and v >= 0 and v < self.c:
                    yield (5, v, 0)
                elif u == self.a and v >= 0 and v < self.c:
                    yield (3, self.c - v - 1, 0)
                elif u >= 0 and u < self.a and v == -1:
                    yield (4, self.a - u  - 1, 0)
                elif u >= 0 and u < self.a and v == self.c:
                    yield (1, u, 0)
            
            elif area == 1:
                if u >= 0 and u < self.a and v >= 0 and v < self.b:
                    yield (1, u, v)
                elif u == -1 and v >= 0 and v < self.b:
                    yield (5, self.c - 1, v)
                elif u == self.a and v >= 0 and v < self.b:
                    yield (3, 0, v)
                elif u >= 0 and u < self.a and v == -1:
                    yield (0, u, self.c - 1)
                elif u >= 0 and u < self.a and v == self.b:
                    yield (2, u, 0)

            elif area == 2:
                if u >= 0 and u < self.a and v >= 0 and v < self.c:
                    yield (2, u, v)
                elif u == -1 and v >= 0 and v < self.c:
                    yield (5, self.c - v - 1, self.b - 1)
                elif u == self.a and v >= 0 and v < self.c:
                    yield (3, v, self.b - 1)
                elif u >= 0 and u < self.a and v == -1:
                    yield (1, u, self.b - 1)
                elif u >= 0 and u < self.a and v == self.c:
                    yield (4, self.a - u - 1, self.b - 1)
            
            elif area == 3:
                if u >= 0 and u < self.c and v >= 0 and v < self.b:
                    yield (3, u, v)
                elif u == -1 and v >= 0 and v < self.b:
                    yield (1, self.a - 1, v)
                elif u == self.c and v >= 0 and v < self.b:
                    yield (4, 0, v)
                elif u >= 0 and u < self.c and v == -1:
                    yield (0, self.a - 1, self.c - u - 1)
                elif u >= 0 and u < self.c and v == self.b:
                    yield (2, self.a - 1, u)
            
            elif area == 4:
                if u >= 0 and u < self.a and v >= 0 and v < self.b:
                    yield (4, u, v)
                elif u == -1 and v >= 0 and v < self.b:
                    yield (3, self.c - 1, v)
                elif u == self.a and v >= 0 and v < self.b:
                    yield (5, 0, v)
                elif u >= 0 and u < self.a and v == -1:
                    yield (0, self.a - u - 1, 0)
                elif u >= 0 and u < self.a and v == self.b:
                    yield (2, self.a - u - 1, self.c - 1)
            
            elif area == 5:
                if u >= 0 and u < self.c and v >= 0 and v < self.b:
                    yield (5, u, v)
                elif u == -1 and v >= 0 and v < self.b:
                    yield (4, self.a - 1, v)
                elif u == self.c and v >= 0 and v < self.b:
                    yield (1, 0, v)
                elif u >= 0 and u < self.c and v == -1:
                    yield (0, 0, u)
                elif u >= 0 and u < self.c and v == self.b:
                    yield (2, 0, self.c - u - 1)

    
def pairs(n):
    return n * (n - 1) // 2
        
    
def solution(cuboid, impassableCells):
    net = CuboidNet(cuboid, impassableCells)
    planet = CuboidPlanet(cuboid, impassableCells)

    net_components = net.connected()
    planet_components = planet.connected()

    net_pairs = sum(pairs(len(component)) for component in net_components)
    planet_pairs = sum(pairs(len(component)) for component in planet_components)

    return planet_pairs - net_pairs

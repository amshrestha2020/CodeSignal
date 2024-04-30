# In a kingdom far, far away, there lives a King Byteasar IX. The history of the kingdom is rich with events and conflicts, most of which is focused on its cities. King Byteasar doesn't want to go down in history as a lame duck ruler, and especially doesn't want to have anything to do with the infamous cities of the kingdom.

# Instead, king Byteasar wants to focus on the roads, which is why he issued a new decree: from now on, all roads are to be considered cities, and all cities are to be considered roads. Now his most grateful subjects must pack up their belongings and move out from the cities to the roads, and the cartographers are busy with building a new roadRegister of the kingdom. All roads of the kingdom are to be named for the cities they connect (i.e. [city1, city2], city1 < city2), sorted lexicographically and enumerated starting from 0. A new road register for such a system needs to be created.

# Your task is to help the cartographers build the new road register. Handle the challenge, and the glorious kingdom of Byteasar IX will never have to deal with its pesky cities ever again!

# Example

# For

# roadRegister = [
#   [false, true,  true,  false, false, false],
#   [true,  false, false, true,  false, false],
#   [true,  false, false, false, false, false],
#   [false, true,  false, false, false, false],
#   [false, false, false, false, false, true ],
#   [false, false, false, false, true,  false]
# ]
# the output should be

# solution(roadRegister) = [
#   [false, true,  true,  false],
#   [true,  false, false, false],
#   [true,  false, false, false],
#   [false, false, false, false]
# ]
# Here's how the new register can be obtained:


def solution(roadRegister):
    # Create a sorted list of tuples representing the roads between cities
    # Each tuple is a pair of cities (i, j) such that there is a road between city i and city j
    roads = sorted({tuple(sorted([i, j])) for i in range(len(roadRegister)) for j in range(len(roadRegister)) if roadRegister[i][j]})
    
    # Create the new road register
    # For each pair of roads (i, j), there is a city in the new road register if and only if roads i and j have a city in common
    new_roadRegister = [[i != j and bool(set(i) & set(j)) for j in roads] for i in roads]
    
    return new_roadRegister

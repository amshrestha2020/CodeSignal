# Once upon a time, in a kingdom far, far away, there lived a King Byteasar VIII. The king went down in history as a great warrior, since he managed to defeat a longtime enemy that had been capturing the kingdom's cities for more than a century. When the war was over, most of the cities were almost completely destroyed, so Byteasar decided to create new cities by merging them.

# The king decided to merge each pair of cities cityi, cityi+1 for i = 0, 2, 4, ... if they were connected by one of the two-way roads running through the kingdom.

# Initially, all information about the roads was stored in the roadRegister. Your task is to return the roadRegister after the merging is performed, assuming that after merging the cities re-indexation is done in such way that any city formed from cities a and b (where a < b) receives index a, and all the cities with numbers i (where i > b) get numbers i - 1.

# Example

# For

# roadRegister = [
#   [false, true,  true,  false, false, false, true ],
#   [true,  false, true,  false, true,  false, false],
#   [true,  true,  false, true,  false, false, true ],
#   [false, false, true,  false, false, true,  true ],
#   [false, true,  false, false, false, false, false],
#   [false, false, false, true,  false, false, false],
#   [true,  false, true,  true,  false, false, false]
# ]
# the output should be

# solution(roadRegister) = [
#   [false, true,  true,  false, true ],
#   [true,  false, false, true,  true ],
#   [true,  false, false, false, false],
#   [false, true,  false, false, false],
#   [true,  true,  false, false, false]
# ]
# Here's how the cities were merged:


import numpy as np

def solution(road_register):
    # Number of cities
    num_cities = len(road_register)
    
    # List to store the cities to be merged
    cities_to_merge = []
    
    # Convert the road register to a numpy array for easier manipulation
    road_register = np.array(road_register)
    
    # Iterate over each pair of cities
    for city1, city2 in ((i, i + 1) for i in range(0, num_cities - num_cities % 2, 2)):
        # If the two cities are connected
        if road_register[city1][city2]:
            # Add the second city to the list of cities to merge
            cities_to_merge.append(city2)
            
            # Disconnect the two cities
            road_register[city1][city2] = road_register[city2][city1] = False
            
            # Merge the roads of the two cities
            road_register[city1] |= road_register[city2]
            road_register[:, city1] |= road_register[:, city2]
    
    # Remove the merged cities from the road register
    road_register = np.delete(road_register, cities_to_merge, 0)
    road_register = np.delete(road_register, cities_to_merge, 1)
    
    return road_register

# Once upon a time, in a kingdom far, far away, there lived a King Byteasar VI. As any king with such a magnificent name, he was destined to leave a trace in history. Unfortunately, imagination wasn't one of Byteasar's strong suits, so the reform he came up with was quite simple: he ordered that all his kingdom's cities should be renamed. He didn't want to come up with new names (as a king, he'd have to remember them all!), so he ordered the cities to swap their names in such a manner that the ith city would have the name of the city number (i + 1)th. The last city in the Byteasar's kingdom would, naturally, get the name of the very first city.

# The cartographers were not happy with this reform, since they had to redraw all the kingdom's maps. Before the reform, information about all the roads between the cities were stored in the roadRegister. Prior to redrawing any map, they had to start with updating the register. Your task is to find out the state of the updated register.

# Example

# For

# roadRegister = [[false, true,  true,  false],
#                 [true,  false, true,  false],
#                 [true,  true,  false, true ],
#                 [false, false, true,  false]]
# the output should be

# solution(roadRegister) = [[false, false, false, true ],
#                           [false, false, true,  true ],
#                           [false, true,  false, true ],
#                           [true,  true,  true,  false]]
# Here's how the catalog can be represented before and after the Great Renaming


def solution(roadRegister):
    # Initialize the updated road register with the same size as the original
    updated_roadRegister = [[False]*len(roadRegister) for _ in range(len(roadRegister))]
    
    # Iterate over each city
    for i in range(len(roadRegister)):
        # Calculate the new name of the city
        new_name = (i + 1) % len(roadRegister)
        
        # Update the roads in the updated road register
        for j in range(len(roadRegister)):
            if roadRegister[i][j]:
                updated_roadRegister[new_name][(j + 1) % len(roadRegister)] = True
                updated_roadRegister[(j + 1) % len(roadRegister)][new_name] = True
    
    return updated_roadRegister

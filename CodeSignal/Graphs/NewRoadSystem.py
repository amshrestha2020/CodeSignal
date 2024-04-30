# Once upon a time, in a kingdom far, far away, there lived a King Byteasar I. As a kind and wise ruler, he did everything in his (unlimited) power to make life for his subjects comfortable and pleasant. One cold evening a messenger arrived at the king's castle with the latest news: all kings in the Kingdoms Union had started enforcing traffic laws! In order to not lose his membership in the Union, King Byteasar decided he must do the same within his kingdom. But what would the citizens think of it?

# The king decided to start introducing the changes with something more or less simple: change all the roads in the kingdom from two-directional to one-directional (one-way). He personally prepared the roadRegister of the new roads, and now he needs to make sure that the road system is convenient and there will be no traffic jams, i.e. each city has the same number of incoming and outgoing roads. As the Hand of the King, you're the one who he has decreed must check his calculations.

# Example

# For

# roadRegister = [[false, true,  false, false],
#                 [false, false, true,  false],
#                 [true,  false, false, true ],
#                 [false, false, true,  false]]
# the output should be
# solution(roadRegister) = true.

# The cities will be connected as follows:


# Cities 0, 1 and 3 (0-based) have one incoming and one outgoing road, and city 2 has two incoming and two outgoing roads. Thus, the output should be true.

# For

# roadRegister = [[false, true,  false, false, false, false, false],
#                 [true,  false, false, false, false, false, false],
#                 [false, false, false, true,  false, false, false],
#                 [false, false, true,  false, false, false, false],
#                 [false, false, false, false, false, false, true ],
#                 [false, false, false, false, true,  false, false],
#                 [false, false, false, false, false, true,  false]]
# the output should be
# solution(roadRegister) = true.

# The cities will be connected as follows:


# Each city has one incoming and one outgoing road.

# For

# roadRegister = [[false, true,  false],
#                 [false, false, false],
#                 [true,  false, false]]
# the output should be
# solution(roadRegister) = false.

# The cities will be connected as follows:


# City 1 has one incoming and no outgoing roads, and city 2 has one outgoing and no incoming roads.

def solution(roadRegister):
    n = len(roadRegister)
    
    # Check for each city
    for city in range(n):
        incoming_roads = sum(roadRegister[i][city] for i in range(n))
        outgoing_roads = sum(roadRegister[city][j] for j in range(n))
        
        # If incoming roads are not equal to outgoing roads, return False
        if incoming_roads != outgoing_roads:
            return False
    
    # All cities have equal incoming and outgoing roads
    return True


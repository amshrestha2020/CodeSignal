# Implement the missing code, denoted by ellipses. You may not modify the pre-existing code.
# A grand Team Chess Tournament will be held at your University. Two teams, smarties and cleveries, will clash to determine whose chess skills are better. The teams have the same number of members, and the ith member of smarties will play against the ith member of cleveries in the ith game for each valid i

# Given the names of the players of both smarties and cleveries, return the games in the order they will be played.

# Example

# For smarties = ["Jane", "Bob", "Peter"] and
# cleveries = ["Oscar", "Lidia", "Ann"], the output should be

# solution(smarties, cleveries) = [["Jane",  "Oscar"],
#                                  ["Bob",   "Lidia"],
#                                  ["Peter", "Ann"]]


def solution(smarties, cleveries):
    return [[smarties[i], cleveries[i]] for i in range(len(smarties))]




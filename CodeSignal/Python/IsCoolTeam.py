# Implement the missing code, denoted by ellipses. You may not modify the pre-existing code.
# You are organizing a team of eSportsmen, and you are determined to make it cool. You are already thinking about winning the world championship: when it happens, the names of your teammates will be chanted one after another by a large audience. You believe that it will sound cool if and only if the first letter of one player's name will be the same as the last letter in the name of the player before them.

# Now you are considering one particular team. Its members are definitely professional gamers, but you're not sure if all together they form a cool team. Implement a function that will check if the team is cool.

# Example

# For team = ["Mark", "Kelly", "Kurt", "Terk"], the output should be
# solution(team) = true.

# The following team announcement will sound cool: "Mark", "Kurt", "Terk", "Kelly".


class Team(object):
    def __init__(self, names):
        self.names = names


    def fixfirst(self, tips):
        # If there's only one name left, return True
        if len(tips) == 1:
            return True
        # If we've seen this combination of names before, return False to avoid infinite recursion
        if tuple(tips) in self.memory:
            return False
        # Count the number of names that start and end with each letter
        check = {}
        for t in tips:
            check[t[0]] = check.get(t[0], 0) - 1
            check[t[1]] = check.get(t[1], 0) + 1
        # If more than two letters have an odd count, return False
        if sum(1 for v in check.values() if v % 2 != 0) > 2:
            return False
        # Try to find a cool arrangement starting from each name
        for i, v in enumerate(tips[1:], 1):
            if v[0] == tips[0][-1] and self.fixfirst([v] + tips[1:i] + tips[i+1:]):
                return True
        # If no cool arrangement is found, add this combination of names to the memory and return False
        self.memory.add(tuple(tips))
        return False

    def __bool__(self):
        # Convert the names to lowercase and create pairs of the first and last letters
        tips = [(name[0].lower(), name[-1].lower()) for name in self.names]
        # Initialize the memory
        self.memory = set()
        # Try to find a cool arrangement starting from each name
        for i, v in enumerate(tips):
            if self.fixfirst([v] + tips[:i] + tips[i+1:]):
                return True
        # If no cool arrangement is found, return False
        return False


def solution(team):
    return bool(Team(team))

# Implement the missing code, denoted by ellipses. You may not modify the pre-existing code.
# You've been training your whole life, and now your dreams finally came true: you are a member of the best Crazyball team in the world! Unfortunately since your team is one of only two teams that play Crazyball, there are already many players in it, including yourself. For the starting lineup on the upcoming game the coach will pick k players, and you're curious if it's possible for you to make it there.

# To calculate the odds of being a starter, you'd like to come up with a list of all possible lineups. Given the list of the players and the number of players k the coach has to pick, return all possible lineups sorted lexicographically. Players in each lineup should also be sorted lexicographically.

# Example

# For players = ["Ninja", "Warrior", "Trainee", "Newbie"] and k = 3,
# the output should be

# solution(players, k) = [["Newbie", "Ninja", "Trainee"], 
#                         ["Newbie", "Ninja", "Warrior"], 
#                         ["Newbie", "Trainee", "Warrior"], 
#                         ["Ninja", "Trainee", "Warrior"]]


from itertools import combinations

def solution(players, k):
    return sorted([sorted(lineup) for lineup in combinations(players, k)])

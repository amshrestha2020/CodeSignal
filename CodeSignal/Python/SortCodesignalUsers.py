# Implement the missing code, denoted by ellipses. You may not modify the pre-existing code.
# At CodeSignal the users can get to the top of the leaderboard by earning XP (experience points) in different modes. The leaderboard is sorted by players XP in descending order, and in case of a tie - by their ids in ascending order.

# Your task is to implement an algorithm that will return the state of the weekly leaderboard given a list of users.

# Example

# For

# users = [["warrior", "1", "1050"],
#          ["Ninja!",  "21", "995"],
#          ["recruit", "3", "995"]]
# the output should be
# solution(users) = ["warrior", "recruit", "Ninja!"].


def solution(users):
    res = [CodeSignalUser(*user) for user in users]
    res.sort(reverse=True)
    return list(map(str, res))



import functools
@functools.total_ordering
class CodeSignalUser:
    def __init__(self, *args):
        self.user_name = args[0]
        self.user_id = int(args[1])
        self.user_xp = int(args[2])
    def __lt__(self, other):
        if self.user_xp < other.user_xp:
            return self.user_xp < other.user_xp
        elif self.user_xp == other.user_xp:
            return self.user_id>other.user_id
        return False
    
    def __str__(self):
        return self.user_name
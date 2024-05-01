# Implement the missing code, denoted by ellipses. You may not modify the pre-existing code.
# Not long ago Greg noticed that he started to forget things, and hurried to the doctor. The doc told him that it was perfectly normal for his age, and wrote down a list of pills that Greg can take in order to improve his memory. He especially recommended one medicine as the most effective one.

# Unfortunately Greg forgot which medicine is the most effective, and he feels like he really needs to take them. Greg recalls that the name of the most effective medicine goes in the list somewhere after the very first name that has an even length. Your task is to help Greg: given the list of the pills, return a list of three names that go right after the very first medicine name of the even length.

# If there are less than three medicines to return, return empty strings instead of them.

# Example

# For pills = ["Notforgetan", "Antimoron", "Rememberin", "Bestmedicen", "Superpillsus"],
# the output should be
# solution(pills) = ["Bestmedicen", "Superpillsus", ""].


from itertools import dropwhile

def solution(pills):
    gen = dropwhile(lambda x: len(x) % 2 != 0, pills + [''] * 3)
    next(gen)
    return [next(gen) for _ in range(3)]

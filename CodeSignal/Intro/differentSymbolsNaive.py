# Given a string, find the number of different characters in it.

# Example

# For s = "cabca", the output should be
# solution(s) = 3.

# There are 3 different characters a, b and c.

def solution(s):
    unique_characters = set(s)
    return len(unique_characters)


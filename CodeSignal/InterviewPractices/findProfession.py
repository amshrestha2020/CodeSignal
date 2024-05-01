# Consider a special family of Engineers and Doctors. This family has the following rules:

# Everybody has two children.
# The first child of an Engineer is an Engineer and the second child is a Doctor.
# The first child of a Doctor is a Doctor and the second child is an Engineer.
# All generations of Doctors and Engineers start with an Engineer.
# We can represent the situation using this diagram:

#                 E
#            /         \
#           E           D
#         /   \        /  \
#        E     D      D    E
#       / \   / \    / \   / \
#      E   D D   E  D   E E   D
# Given the level and position of a person in the ancestor tree above, find the profession of the person.
# Note: in this tree first child is considered as left child, second - as right.

# Example

# For level = 3 and pos = 3, the output should be
# solution(level, pos) = "Doctor".

def solution(level, pos):
    if level == 1:
        return "Engineer"
    if pos <= 2**(level - 2):
        return solution(level - 1, pos)
    else:
        return "Doctor" if solution(level - 1, pos - 2**(level - 2)) == "Engineer" else "Engineer"

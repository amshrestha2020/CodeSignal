# Given two binary trees t1 and t2, determine whether the second tree is a subtree of the first tree. A subtree for vertex v in a binary tree t is a tree consisting of v and all its descendants in t. Determine whether or not there is a vertex v (possibly none) in tree t1 such that a subtree for vertex v (possibly empty) in t1 equals t2.

# Example

# For

# t1 = {
#     "value": 5,
#     "left": {
#         "value": 10,
#         "left": {
#             "value": 4,
#             "left": {
#                 "value": 1,
#                 "left": null,
#                 "right": null
#             },
#             "right": {
#                 "value": 2,
#                 "left": null,
#                 "right": null
#             }
#         },
#         "right": {
#             "value": 6,
#             "left": null,
#             "right": {
#                 "value": -1,
#                 "left": null,
#                 "right": null
#             }
#         }
#     },
#     "right": {
#         "value": 7,
#         "left": null,
#         "right": null
#     }
# }
# and

# t2 = {
#     "value": 10,
#     "left": {
#         "value": 4,
#         "left": {
#             "value": 1,
#             "left": null,
#             "right": null
#         },
#         "right": {
#             "value": 2,
#             "left": null,
#             "right": null
#         }
#     },
#     "right": {
#         "value": 6,
#         "left": null,
#         "right": {
#             "value": -1,
#             "left": null,
#             "right": null
#         }
#     }
# }
# the output should be solution(t1, t2) = true.

# This is what these trees look like:

#       t1:             t2:
#        5              10
#       / \            /  \
#     10   7          4    6
#    /  \            / \    \
#   4    6          1   2   -1
#  / \    \
# 1   2   -1
# As you can see, t2 is a subtree of t1 (the vertex in t1 with value 10).

# For

# t1 = {
#     "value": 5,
#     "left": {
#         "value": 10,
#         "left": {
#             "value": 4,
#             "left": {
#                 "value": 1,
#                 "left": null,
#                 "right": null
#             },
#             "right": {
#                 "value": 2,
#                 "left": null,
#                 "right": null
#             }
#         },
#         "right": {
#             "value": 6,
#             "left": {
#                 "value": -1,
#                 "left": null,
#                 "right": null
#             },
#             "right": null
#         }
#     },
#     "right": {
#         "value": 7,
#         "left": null,
#         "right": null
#     }
# }
# and

# t2 = {
#     "value": 10,
#     "left": {
#         "value": 4,
#         "left": {
#             "value": 1,
#             "left": null,
#             "right": null
#         },
#         "right": {
#             "value": 2,
#             "left": null,
#             "right": null
#         }
#     },
#     "right": {
#         "value": 6,
#         "left": null,
#         "right": {
#             "value": -1,
#             "left": null,
#             "right": null
#         }
#     }
# }
# the output should be solution(t1, t2) = false.

# This is what these trees look like:

#         t1:            t2:
#          5             10
#        /   \          /  \
#      10     7        4    6
#    /    \           / \    \
#   4     6          1   2   -1
#  / \   / 
# 1   2 -1
# As you can see, there is no vertex v such that the subtree of t1 for vertex v equals t2.

# For

# t1 = {
#     "value": 1,
#     "left": {
#         "value": 2,
#         "left": null,
#         "right": null
#     },
#     "right": {
#         "value": 2,
#         "left": null,
#         "right": null
#     }
# }
# and

# t2 = {
#     "value": 2,
#     "left": {
#         "value": 1,
#         "left": null,
#         "right": null
#     },
#     "right": null
# }
# the output should be solution(t1, t2) = false.

#
# Binary trees are already defined with this interface:
# class Tree(object):
#   def __init__(self, x):
#     self.value = x
#     self.left = None
#     self.right = None


class Tree:
    def __init__(self, value=0, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

def is_identical(t1, t2):
    if t1 is None and t2 is None:
        return True
    if t1 is None or t2 is None:
        return False
    return (t1.value == t2.value) and is_identical(t1.left, t2.left) and is_identical(t1.right, t2.right)

def solution(t1, t2):
    if t2 is None:
        return True
    if t1 is None:
        return False
    if is_identical(t1, t2):
        return True
    return solution(t1.left, t2) or solution(t1.right, t2)
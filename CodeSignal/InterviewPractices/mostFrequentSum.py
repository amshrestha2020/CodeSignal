# The sum of a subtree is the sum of all the node values in that subtree, including its root.

# Given a binary tree of integers, find the most frequent sum (or sums) of its subtrees.

# Example

# For
# t = {
#     "value": 1,
#     "left": {
#         "value": 2,
#         "left": null,
#         "right": null
#     },
#     "right": {
#         "value": 3,
#         "left": null,
#         "right": null
#     }
# }
# the output should be
# solution(t) = [2, 3, 6].
# 1st example

# Since all the sum values in this tree occur only once, return all of them in ascending order.

# For
# t = {
#     "value": -2,
#     "left": {
#         "value": -3,
#         "left": null,
#         "right": null
#     },
#     "right": {
#         "value": 2,
#         "left": null,
#         "right": null
#     }
# }
# the output should be
# solution(t) = [-3].
# 2nd example

# There are 3 subtree sums for this tree: -2 + (-3) + 2 = -3, -3, and -2. The most frequent sum is -3 since it appears twice.

#
# Binary trees are already defined with this interface:
# class Tree(object):
#   def __init__(self, x):
#     self.value = x
#     self.left = None
#     self.right = None

from collections import defaultdict, Counter

class Node:
    def __init__(self, x):
        self.value = x
        self.left = None
        self.right = None

def solution(t):
    if not t:
        return []

    def dfs(node):
        if node is None:
            return 0
        s = node.value + dfs(node.left) + dfs(node.right)
        count[s] += 1
        return s

    count = Counter()
    dfs(t)
    max_freq = max(count.values())
    result = [s for s, v in count.items() if v == max_freq]
    return sorted(result)  # sort the result before returning

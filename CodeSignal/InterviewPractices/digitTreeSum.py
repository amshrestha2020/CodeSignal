# We're going to store numbers in a tree. Each node in this tree will store a single digit (from 0 to 9), and each path from root to leaf encodes a non-negative integer.

# Given a binary tree t, find the sum of all the numbers encoded in it.

# Example

# For
# t = {
#     "value": 1,
#     "left": {
#         "value": 0,
#         "left": {
#             "value": 3,
#             "left": null,
#             "right": null
#         },
#         "right": {
#             "value": 1,
#             "left": null,
#             "right": null
#         }
#     },
#     "right": {
#         "value": 4,
#         "left": null,
#         "right": null
#     }
# }
# the output should be
# solution(t) = 218.
# There are 3 numbers encoded in this tree:

# Path 1->0->3 encodes 103
# Path 1->0->1 encodes 101
# Path 1->4 encodes 14
# and their sum is 103 + 101 + 14 = 218.
# t = {
#     "value": 0,
#     "left": {
#         "value": 9,
#         "left": null,
#         "right": null
#     },
#     "right": {
#         "value": 9,
#         "left": {
#             "value": 1,
#             "left": null,
#             "right": null
#         },
#         "right": {
#             "value": 3,
#             "left": null,
#             "right": null
#         }
#     }
# }
# the output should be
# solution(t) = 193.
# Because 09 + 091 + 093 = 193



# Binary trees are already defined with this interface:
class Tree(object):
  def __init__(self, x):
    self.value = x
    self.left = None
    self.right = None
    
def solution(t):
    def dfs(node, path_sum):
        if not node:
            return 0
        path_sum = path_sum * 10 + node.value
        if not node.left and not node.right:
            return path_sum
        return dfs(node.left, path_sum) + dfs(node.right, path_sum)

    return dfs(t, 0)
# Given a binary tree t and an integer s, determine whether there is a root to leaf path in t such that the sum of vertex values equals s.

# Example

# For

# t = {
#     "value": 4,
#     "left": {
#         "value": 1,
#         "left": {
#             "value": -2,
#             "left": null,
#             "right": {
#                 "value": 3,
#                 "left": null,
#                 "right": null
#             }
#         },
#         "right": null
#     },
#     "right": {
#         "value": 3,
#         "left": {
#             "value": 1,
#             "left": null,
#             "right": null
#         },
#         "right": {
#             "value": 2,
#             "left": {
#                 "value": -2,
#                 "left": null,
#                 "right": null
#             },
#             "right": {
#                 "value": -3,
#                 "left": null,
#                 "right": null
#             }
#         }
#     }
# }
# and
# s = 7,
# the output should be solution(t, s) = true.

# This is what this tree looks like:

#       4
#      / \
#     1   3
#    /   / \
#   -2  1   2
#     \    / \
#      3  -2 -3
# Path 4 -> 3 -> 2 -> -2 gives us 7, the required sum.

# For

# t = {
#     "value": 4,
#     "left": {
#         "value": 1,
#         "left": {
#             "value": -2,
#             "left": null,
#             "right": {
#                 "value": 3,
#                 "left": null,
#                 "right": null
#             }
#         },
#         "right": null
#     },
#     "right": {
#         "value": 3,
#         "left": {
#             "value": 1,
#             "left": null,
#             "right": null
#         },
#         "right": {
#             "value": 2,
#             "left": {
#                 "value": -4,
#                 "left": null,
#                 "right": null
#             },
#             "right": {
#                 "value": -3,
#                 "left": null,
#                 "right": null
#             }
#         }
#     }
# }
# and
# s = 7,
# the output should be solution(t, s) = false.

# This is what this tree looks like:

#       4
#      / \
#     1   3
#    /   / \
#   -2  1   2
#     \    / \
#      3  -4 -3
# There is no path from root to leaf with the given sum 7.


# Binary trees are already defined with this interface:
# class Tree(object):
#   def __init__(self, x):
#     self.value = x
#     self.left = None
#     self.right = None

def solution(t, s):
    # Base case: if the tree is empty, return False
    if not t:
        return False
    
    # Recursive DFS function to traverse the tree
    def dfs(node, target):
        # If the current node is a leaf node
        if not node.left and not node.right:
            # Check if the remaining target sum equals the leaf node value
            return target - node.value == 0
        # Recursive calls for left and right subtrees
        left_path = dfs(node.left, target - node.value) if node.left else False
        right_path = dfs(node.right, target - node.value) if node.right else False
        # Return True if either left or right subtree has a valid path
        return left_path or right_path
    
    # Start DFS from the root of the binary tree
    return dfs(t, s)

# Test cases
t1 = Tree(4)
t1.left = Tree(1)
t1.left.left = Tree(-2)
t1.left.left.right = Tree(3)
t1.right = Tree(3)
t1.right.left = Tree(1)
t1.right.right = Tree(2)
t1.right.right.left = Tree(-2)
t1.right.right.right = Tree(-3)
print(solution(t1, 7))  # Output: True

t2 = Tree(4)
t2.left = Tree(1)
t2.left.left = Tree(-2)
t2.left.left.right = Tree(3)
t2.right = Tree(3)
t2.right.left = Tree(1)
t2.right.right = Tree(2)
t2.right.right.left = Tree(-4)
t2.right.right.right = Tree(-3)
print(solution(t2, 7))  # Output: False


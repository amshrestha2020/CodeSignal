# Given a binary tree t, determine whether it is symmetric around its center, i.e. each side mirrors the other.

# Example

# For

# t = {
#     "value": 1,
#     "left": {
#         "value": 2,
#         "left": {
#             "value": 3,
#             "left": null,
#             "right": null
#         },
#         "right": {
#             "value": 4,
#             "left": null,
#             "right": null
#         }
#     },
#     "right": {
#         "value": 2,
#         "left": {
#             "value": 4,
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
# the output should be solution(t) = true.

# Here's what the tree in this example looks like:

#     1
#    / \
#   2   2
#  / \ / \
# 3  4 4  3
# As you can see, it is symmetric.

# For

# t = {
#     "value": 1,
#     "left": {
#         "value": 2,
#         "left": null,
#         "right": {
#             "value": 3,
#             "left": null,
#             "right": null
#         }
#     },
#     "right": {
#         "value": 2,
#         "left": null,
#         "right": {
#             "value": 3,
#             "left": null,
#             "right": null
#         }
#     }
# }
# the output should be solution(t) = false.

# Here's what the tree in this example looks like:

#     1
#    / \
#   2   2
#    \   \
#    3    3
# As you can see, it is not symmetric.


# Binary trees are already defined with this interface:
# class Tree(object):
#   def __init__(self, x):
#     self.value = x
#     self.left = None
#     self.right = None

def solution(t):
    # Helper function to check if two trees are symmetric
    def is_symmetric(left, right):
        # Base case: if both nodes are None, they are symmetric
        if not left and not right:
            return True
        # If one node is None but the other is not, they are not symmetric
        if not left or not right:
            return False
        # Check if values are equal and subtrees are symmetric
        return left.value == right.value and \
               is_symmetric(left.left, right.right) and \
               is_symmetric(left.right, right.left)
    
    # Start DFS from the root of the binary tree
    return is_symmetric(t, t)

# Test cases
t1 = Tree(1)
t1.left = Tree(2)
t1.left.left = Tree(3)
t1.left.right = Tree(4)
t1.right = Tree(2)
t1.right.left = Tree(4)
t1.right.right = Tree(3)
print(solution(t1))  # Output: True

t2 = Tree(1)
t2.left = Tree(2)
t2.left.right = Tree(3)
t2.right = Tree(2)
t2.right.right = Tree(3)
print(solution(t2))  # Output: False

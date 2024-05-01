# A tree is considered a binary search tree (BST) if for each of its nodes the following is true:

# The left subtree of a node contains only nodes with keys less than the node's key.
# The right subtree of a node contains only nodes with keys greater than the node's key.
# Both the left and the right subtrees must also be binary search trees.
# Removing a value x from a BST t is done in the following way:

# If there is no x in t, nothing happens;
# Otherwise, let t' be a subtree of t such that t'.value = x.
# If t' has a left subtree, remove the rightmost node from it and put it at the root of t';
# Otherwise, remove the root of t' and its right subtree becomes the new t's root.
# For example, removing 4 from the following tree has no effect because there is no such value in the tree:

#     5
#    / \
#   2   6
#  / \   \
# 1   3   8
#        /
#       7
# Removing 5 causes 3 (the rightmost node in left subtree) to move to the root:

#     3
#    / \
#   2   6
#  /     \
# 1       8
#        /
#       7
# And removing 6 after that creates the following tree:

#     3
#    / \
#   2   8
#  /   /
# 1   7
# You're given a binary search tree t and an array of numbers queries. Your task is to remove queries[0], queries[1], etc., from t, step by step, following the algorithm above. Return the resulting BST.


#
# Binary trees are already defined with this interface:
# class Tree(object):
#   def __init__(self, x):
#     self.value = x
#     self.left = None
#     self.right = None

class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def remove_node(node, value):
    if node is None:
        return None
    
    if value < node.value:
        node.left = remove_node(node.left, value)
    elif value > node.value:
        node.right = remove_node(node.right, value)
    else:
        if node.left is None:
            return node.right
        elif node.right is None:
            return node.left
        else:
            temp = node.left
            while temp.right:
                temp = temp.right
            node.value = temp.value
            node.left = remove_node(node.left, temp.value)
    return node

def solution(t, queries):
    if t is None:
        return None
    
    for query in queries:
        t = remove_node(t, query)
    return t

# Example usage:
t = TreeNode(3)
t.left = TreeNode(2)
t.right = TreeNode(5)

queries = [2, 3, 0, 5]
result = solution(t, queries)
print(result)  # Output: None


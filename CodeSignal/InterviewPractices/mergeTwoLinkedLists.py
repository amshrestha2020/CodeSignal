# Note: Your solution should have O(l1.length + l2.length) time complexity, since this is what you will be asked to accomplish in an interview.

# Given two singly linked lists sorted in non-decreasing order, your task is to merge them. In other words, return a singly linked list, also sorted in non-decreasing order, that contains the elements from both original lists.

# Example

# For l1 = [1, 2, 3] and l2 = [4, 5, 6], the output should be
# solution(l1, l2) = [1, 2, 3, 4, 5, 6];
# For l1 = [1, 1, 2, 4] and l2 = [0, 3, 5], the output should be
# solution(l1, l2) = [0, 1, 1, 2, 3, 4, 5].


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.value = x
#         self.next = None

def solution(l1, l2):
    # Create a dummy node
    dummy = ListNode(0)
    current = dummy

    while l1 and l2:
        if l1.value < l2.value:
            current.next = l1
            l1 = l1.next
        else:
            current.next = l2
            l2 = l2.next
        current = current.next

    # If there are remaining nodes in either list, append them
    if l1:
        current.next = l1
    else:
        current.next = l2

    # Return the merged list, excluding the dummy node
    return dummy.next

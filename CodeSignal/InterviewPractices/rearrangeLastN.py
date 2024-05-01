# Note: Try to solve this task in O(list size) time using O(1) additional space, since this is what you'll be asked during an interview.

# Given a singly linked list of integers l and a non-negative integer n, move the last n list nodes to the beginning of the linked list.

# Example

# For l = [1, 2, 3, 4, 5] and n = 3, the output should be
# solution(l, n) = [3, 4, 5, 1, 2];
# For l = [1, 2, 3, 4, 5, 6, 7] and n = 1, the output should be
# solution(l, n) = [7, 1, 2, 3, 4, 5, 6].


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.value = x
#         self.next = None

def solution(l, n):
    if not l or n == 0:
        return l

    # Initialize pointers
    first = l
    second = l

    # Move the first pointer n nodes ahead in the linked list
    for _ in range(n):
        first = first.next

    # If the first pointer reached the end of the list, return the list as is
    if not first:
        return l

    # Move the first pointer to the end of the list
    # and the second pointer to the node before the section to be moved
    while first.next:
        first = first.next
        second = second.next

    # Reconnect the nodes in the correct order
    new_head = second.next
    second.next = None
    first.next = l

    return new_head

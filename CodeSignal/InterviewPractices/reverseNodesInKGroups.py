# Note: Your solution should have O(n) time complexity, where n is the number of elements in l, and O(1) additional space complexity, since this is what you would be asked to accomplish in an interview.

# Given a linked list l, reverse its nodes k at a time and return the modified list. k is a positive integer that is less than or equal to the length of l. If the number of nodes in the linked list is not a multiple of k, then the nodes that are left out at the end should remain as-is.

# You may not alter the values in the nodes - only the nodes themselves can be changed.

# Example

# For l = [1, 2, 3, 4, 5] and k = 2, the output should be
# solution(l, k) = [2, 1, 4, 3, 5];
# For l = [1, 2, 3, 4, 5] and k = 1, the output should be
# solution(l, k) = [1, 2, 3, 4, 5];
# For l = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11] and k = 3, the output should be
# solution(l, k) = [3, 2, 1, 6, 5, 4, 9, 8, 7, 10, 11].



# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.value = x
#         self.next = None


class ListNode:
    def __init__(self, value=0, next=None):
        self.value = value
        self.next = next

def solution(l, k):
    # Helper function to reverse a linked list
    def reverse_linked_list(start, end):
        prev = None
        curr = start
        while curr != end:
            next_node = curr.next
            curr.next = prev
            prev = curr
            curr = next_node
        return prev

    dummy = ListNode(0)
    dummy.next = l
    prev_group_end = dummy
    while True:
        # Find the start and end of the next group
        group_start = prev_group_end.next
        group_end = group_start
        for _ in range(k - 1):
            if group_end is None:
                return dummy.next  # End of the list, no more groups to reverse
            group_end = group_end.next

        if group_end is None:
            return dummy.next  # End of the list, no more groups to reverse

        # Reverse the current group and connect it with the previous group
        next_group_start = group_end.next
        new_group_start = reverse_linked_list(group_start, next_group_start)
        prev_group_end.next = new_group_start
        group_start.next = next_group_start

        # Move prev_group_end to the end of the current group
        prev_group_end = group_start

    return dummy.next


# You're given 2 huge integers represented by linked lists. Each linked list element is a number from 0 to 9999 that represents a number with exactly 4 digits. The represented number might have leading zeros. Your task is to add up these huge integers and return the result in the same format.

# Example

# For a = [9876, 5432, 1999] and b = [1, 8001], the output should be
# solution(a, b) = [9876, 5434, 0].

# Explanation: 987654321999 + 18001 = 987654340000.

# For a = [123, 4, 5] and b = [100, 100, 100], the output should be
# solution(a, b) = [223, 104, 105].

# Explanation: 12300040005 + 10001000100 = 22301040105.


# Singly-linked lists are already defined with this interface:
# class ListNode(object):
#   def __init__(self, x):
#     self.value = x
#     self.next = None
#


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.value = x
#         self.next = None

def solution(a, b):
    # Convert linked lists to integers
    num1 = linked_list_to_int(a)
    num2 = linked_list_to_int(b)

    # Add the integers
    sum = num1 + num2

    # Convert the sum back to linked list format
    result = int_to_linked_list(sum)

    return result

def linked_list_to_int(node):
    num = 0
    while node:
        num = num * 10000 + node.value
        node = node.next
    return num

def int_to_linked_list(num):
    # Create a dummy node
    dummy = ListNode(0)
    current = dummy

    if num == 0:
        return ListNode(0)

    while num > 0:
        current.next = ListNode(num % 10000)
        num //= 10000
        current = current.next

    # Reverse the linked list and return
    return reverse(dummy.next)

def reverse(node):
    prev = None
    while node:
        next_node = node.next
        node.next = prev
        prev = node
        node = next_node
    return prev

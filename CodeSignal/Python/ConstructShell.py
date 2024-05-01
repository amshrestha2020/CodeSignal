# Implement the missing code, denoted by ellipses. You may not modify the pre-existing code.
# A 2D list lst of size 2 * n - 1 is called a shell if it is filled with zeros and has the following configuration:

# lst[0] contains one element;
# lst[1] contains two elements;
# ...
# lst[n - 2] contains n - 1 elements;
# lst[n - 1] contains n elements;
# lst[n] contains n - 1 elements;
# ...
# lst[2 * n - 3] contains two elements;
# lst[2 * n - 2] contains one element.
# Given an integer n, return a shell list.

# Example

# For n = 3, the output should be

# solution(n) = [[0],
#                [0, 0],
#                [0, 0, 0],
#                [0, 0],
#                [0]]

def solution(n):
    return [[0] * (i + 1) for i in range(n)] + [[0] * (i + 1) for i in range(n - 2, -1, -1)]

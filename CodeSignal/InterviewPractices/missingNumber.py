# You are supposed to label a bunch of boxes with numbers from 0 to n inclusive, and all the labels are stored in the array arr. Unfortunately one of the labels is missing. Your task is to find it.

# Example

# For arr = [3, 1, 0], the output should be solution(arr) = 2.

# For arr = [0], the output should be solution(arr) = 1.

# Explanation:
# Boxes should be labeled from 0 to 1 inclusive, so in this case the missing label is 1.


def solution(arr):
    n = len(arr)
    total = n * (n + 1) // 2
    return total - sum(arr)

# Two arrays are called similar if one can be obtained from another by swapping at most one pair of elements in one of the arrays.

# Given two arrays a and b, check whether they are similar.

# Example

# For a = [1, 2, 3] and b = [1, 2, 3], the output should be
# solution(a, b) = true.

# The arrays are equal, no need to swap any elements.

# For a = [1, 2, 3] and b = [2, 1, 3], the output should be
# solution(a, b) = true.

# We can obtain b from a by swapping 2 and 1 in b.

# For a = [1, 2, 2] and b = [2, 1, 1], the output should be
# solution(a, b) = false.

# Any swap of any two elements either in a or in b won't make a and b equal.


def solution(a, b):
    # Count the number of differences between the arrays
    diff_count = sum(1 for ai, bi in zip(a, b) if ai != bi)

    # Check if there are zero differences or two differences with elements in reverse order
    return diff_count == 0 or (diff_count == 2 and sorted(a) == sorted(b))

    


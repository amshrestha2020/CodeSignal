# Implement the missing code, denoted by ellipses. You may not modify the pre-existing code.
# You are given an array of integers. Sort its sub-array between the given indices l and r (inclusive) and leave the other elements intact.

# Example

# For a = [5, 2, 1, 7, 5, 3, 2, 3], l = 0, and r = 3, the output should be
# solution(a, l, r) = [1, 2, 5, 7, 5, 3, 2, 3].

def solution(a, l, r):

    if l >= r:
        return a

    x = a[l]
    i = l
    j = r

    while i <= j:
        while a[i] < x:
            i += 1
        while a[j] > x:
            j -= 1
        if i <= j:
            t = a[i]
            a[i] = a[j]
            a[j] = t
            i += 1
            j -= 1

    solution(a, l, j)
    solution(a, i, r)

    return a

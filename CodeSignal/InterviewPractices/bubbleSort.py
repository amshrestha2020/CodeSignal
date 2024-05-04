# Implement the missing code, denoted by ellipses. You may not modify the pre-existing code.
# Given an array of integers, sort it.

# Example

# For items = [2, 4, 1, 5], the output should be
# solution(items) = [1, 2, 4, 5].


def solution(items):

    def swap(firstIndex, secondIndex):
        temp = items[firstIndex]
        items[firstIndex] = items[secondIndex]
        items[secondIndex] = temp

    length = len(items)

    for i in range(length):
        j = 0
        stop = length - i
        while j < stop - 1:
            if items[j] > items[j + 1]:
                swap(j, j + 1)
            j += 1
    return items

# Given array of integers, for each position i, search among the previous positions for the last (from the left) position that contains a smaller value. Store this value at position i in the answer. If no such value can be found, store -1 instead.

# Example

# For items = [3, 5, 2, 4, 5], the output should be
# solution(items) = [-1, 3, -1, 2, 4].

def solution(items):
    res = []

    for i in range(len(items)):
        for j in range(i - 1, -1, -1):
            if items[j] < items[i]:
                res.append(items[j])
                break
        else:
            res.append(-1)

    return res

# Given a string str and array of pairs that indicates which indices in the string can be swapped, return the lexicographically largest string that results from doing the allowed swaps. You can swap indices any number of times.

# Example

# For str = "abdc" and pairs = [[1, 4], [3, 4]], the output should be
# solution(str, pairs) = "dbca".

# By swapping the given indices, you get the strings: "cbda", "cbad", "dbac", "dbca". The lexicographically largest string in this list is "dbca".



def solution(s, pairs):
    if not pairs: return s

    # Convert 1-based indices to 0-based
    pairs = [[x-1, y-1] for x, y in pairs]

    # Initialize parent array for union-find
    parent = list(range(len(s)))

    def find(x):
        if x != parent[x]:
            parent[x] = find(parent[x])
        return parent[x]

    def union(x, y):
        parent[find(x)] = find(y)

    # Union pairs
    for x, y in pairs:
        union(x, y)

    # Group indices that can be swapped
    groups = [[] for _ in range(len(s))]
    for i, x in enumerate(parent):
        groups[find(x)].append(i)

    # Sort characters in each group in descending order
    for group in groups:
        group.sort(key=lambda x: -ord(s[x]))

    # Build the result string
    result = list(s)
    for group in groups:
        for i, j in enumerate(sorted(group)):
            result[j] = s[group[i]]

    return ''.join(result)

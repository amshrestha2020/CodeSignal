# Given an array of equal-length strings, you'd like to know if it's possible to rearrange the order of the elements in such a way that each consecutive pair of strings differ by exactly one character. Return true if it's possible, and false if not.

# Note: You're only rearranging the order of the strings, not the order of the letters within the strings!

# Example

# For inputArray = ["aba", "bbb", "bab"], the output should be
# solution(inputArray) = false.

# There are 6 possible arrangements for these strings:

# ["aba", "bbb", "bab"]
# ["aba", "bab", "bbb"]
# ["bbb", "aba", "bab"]
# ["bbb", "bab", "aba"]
# ["bab", "bbb", "aba"]
# ["bab", "aba", "bbb"]
# None of these satisfy the condition of consecutive strings differing by 1 character, so the answer is false.

# For inputArray = ["ab", "bb", "aa"], the output should be
# solution(inputArray) = true.

# It's possible to arrange these strings in a way that each consecutive pair of strings differ by 1 character (eg: "aa", "ab", "bb" or "bb", "ab", "aa"), so return true.

def difference_by_one(s1, s2):
    return sum(c1 != c2 for c1, c2 in zip(s1, s2)) == 1

def is_valid_path(path, graph):
    for i in range(1, len(path)):
        if path[i] not in graph[path[i - 1]]:
            return False
    return True

def solution(inputArray):
    n = len(inputArray)

    # Build the graph based on the difference by one character
    graph = {i: [] for i in range(n)}
    for i in range(n):
        for j in range(i + 1, n):
            if difference_by_one(inputArray[i], inputArray[j]):
                graph[i].append(j)
                graph[j].append(i)

    # Backtracking to check all possible arrangements
    def backtrack(path):
        if len(path) == n:
            return is_valid_path(path, graph)

        for node in graph[path[-1]]:
            if node not in path:
                path.append(node)
                if backtrack(path):
                    return True
                path.pop()

        return False

    # Try all possible starting nodes
    for start_node in range(n):
        if backtrack([start_node]):
            return True

    return False


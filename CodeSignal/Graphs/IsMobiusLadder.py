# You've been studying trees a lot lately, and became an expert in caterpillar trees. Now that you know everything about them, you're ready to climb one. However, in order to climb such tree you need a special ladder that you call a mobius ladder.

# A mobius ladder is a slightly modified proper ladder. Firstly, let's define what proper ladder is: a proper ladder is a ladder that can be represented by a graph containing two chains of vertices with n vertices in each one, where the ith vertex of the first chain is connected to the ith vertex of the second chain. For example, a proper ladder with 8 vertices looks like this:



# A mobius ladder is a proper ladder with two more connections: the first vertex of the first chain is connected to the last vertex of the second chain, and last vertex of the first chain is connected to the first vertex of the second chain. For example, here is a mobius ladder with 8 vertices:



# You found a ladder that can be represented by n vertices in the attic. Now you need to check if it is a mobius ladder, to make sure it can be used to climb a caterpillar tree.

# Example

# For n = 6 and ladder = [[0, 1], [1, 2], [2, 3], [3, 4], [4, 5], [5, 0]], the output should be
# solution(n, ladder) = false.



# For n = 8 and

# ladder = [[0, 1], [0, 2], [0, 7], [1, 3], [1, 6], [2, 3],
#           [2, 4], [3, 5], [4, 5], [4, 6], [5, 7], [6, 7]]
# the output should be solution(n, ladder) = true.

# This is the test from the description:



# For n = 10 and

# ladder = [[0, 1], [0, 3], [0, 7], [0, 9], [1, 2],
#           [1, 4], [1, 8], [2, 3], [2, 5], [2, 9],
#           [3, 4], [3, 6], [4, 5], [4, 7], [5, 6],
#           [5, 8], [6, 7], [6, 9], [7, 8], [8, 9]]
# the output should be solution(n, ladder) = false.


def solution(n, ladder):
    def get_bottom_two_rungs():
        options = []

        if len(adj[0]) != 3:
            return options

        poss = list(adj[0])
        for i in range(3):
            for j in range(3):
                if i != j:
                    up = poss[i]
                    right = poss[j]

                    mutual_neighbors = (adj[up] & adj[right]) - {0}
                    if not mutual_neighbors:
                        continue

                    for diag in mutual_neighbors:
                        options.append([[0, right], [up, diag]])
        return options

    def can_build_ladder_with_rungs(first, second):
        max_row = n//2 + 1
        matrix = [[-1, -1] for _ in range(max_row)]

        matrix[0] = first
        matrix[1] = second

        seen = set(first) | set(second)

        for row in range(2, max_row):
            a, b = matrix[row-1]
            c, d = matrix[row-2]

            poss1 = adj[a] - {b, c}
            if len(poss1) != 1:
                print('not poss 1', row, poss1)
                return False
            val = poss1.pop()
            seen.add(val)
            matrix[row][0] = val

            poss2 = adj[b] - {a, d}
            if len(poss2) != 1:
                print('not poss 2', row, poss2)
                return False
            val2 = poss2.pop()
            if val not in adj[val2]:
                return False
            seen.add(val2)
            matrix[row][1] = val2

        return matrix[-1][::-1] == matrix[0]

    adj = {k: set() for k in range(n)}

    for x, y in ladder:
        adj[x].add(y)
        adj[y].add(x)

    if n == 2:
        return adj[0] == {1} and adj[1] == {0}

    if len(adj[0]) != 3:
        return False

    for opt in get_bottom_two_rungs():
        if can_build_ladder_with_rungs(*opt):
            return True
    return False


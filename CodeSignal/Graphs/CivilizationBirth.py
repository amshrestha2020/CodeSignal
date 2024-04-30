# You are the leader of a tribe living on a remote archipelago. It looks like your tribe is lagging behind the most modern civilizations, so it's about time you start to get closer to them. In order to do this, you decided to start enforcing new laws.

# As a smart ruler, you came up with all the laws yourself and numbered them from 1 to count in the order of decreasing importance. You're also a generous leader, so you allowed the aborigines to chose the laws that should be enacted. Each aborigines chose two laws that most important to them, and voted either for or against them.

# Fairness is also one of your many good traits, so you want to satisfy every aborigine on your island. An aborigine will be satisfied if at least one of his proposals is taken, i.e. either one of the laws he voted for is enacted, or one of those he voted against is not enacted.

# Given the votes array denoting aborigines' votes and the number of laws count, implement a function that will determine which laws should be enacted to satisfy the entire tribe. If there are several solutions, choose the one with the first law (the most important one) enacted. If there are still several options, chose the one with the first law enacted, and so on.

# Example

# For count = 2 and

# votes = [[ 1,  2],
#          [ 1, -2],
#          [-2, -1]]
# , the output should be
# solution(count, votes) = [1, 0].

# The first aborigine wants the first and the second law be enacted. The second aborigine wants the first law be enacted and doesn't want the second law be enacted. The third aborigine doesn't want the first and and the second laws be enacted. The optimal solution is thus to enact the first law and leave out the second law.


def solution(count, votes):
    from collections import defaultdict as ddict
    
    # Initialize graph and law dictionary
    g = ddict(lambda: [[], []])
    law = ddict(lambda: -1)
    
    # Populate the graph based on aborigines' votes
    for index, (x, y) in enumerate(votes):
        g[abs(x)][x > 0].append(index)
        g[abs(y)][y > 0].append(index)
    
    # Convert votes to sets for efficient operations
    votes = list(map(set, votes))
    
    # Recursive function to determine if a law can be enacted
    def setting(pos, enact, tmp):
        enact ^= 1
        curr = pos if enact else -pos
        for person in g[pos][enact]:
            choice = votes[person] - {curr}
            if not choice:
                return 0
            choice = choice.pop()
            if tmp[abs(choice)] == -1:
                tmp[abs(choice)] = choice > 0
                if not setting(abs(choice), choice > 0, tmp):
                    return 0
            else:
                if tmp[abs(choice)] != (choice > 0):
                    return 0
        return 1
    
    # Try to set laws based on aborigines' preferences
    for i in range(1, count + 1):
        if setting(i, 1, law.copy()):
            law[i] = 1
        elif setting(i, 0, law.copy()):
            law[i] = 0
        else:
            return [-1] * count
    
    return list(law.values())

# Example usage
count = 2
votes = [[1, 2], [1, -2], [-2, -1]]
print(solution(count, votes))  # Output: [1, 0]

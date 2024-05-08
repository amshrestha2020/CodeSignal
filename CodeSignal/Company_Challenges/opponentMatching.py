# When you click the VS Fight button on CodeSignal, the system tries to match you with the best opponent possible. The matching algorithm has become more complex over time,but initially it was a simple search for someone whose xp is as close to yours as possible.

# The easiest way to understand how it used to conduct the search is as follows:



# Imagine that each user looking for an opponent is standing at the center of a search circle on a horizontal xp axis.
# All the search circles have the same radius (the search radius), and initially search radius is equal to 0.
# At each step, the search radius is increased by 1.
# A match is found as soon as two search circles intersect. These circles are then removed immediately.
# For the sake of simplicity, assume that on each step no more than one pair of circles can intersect.
# Given a list of requests as user xps, match them up using the algorithm described above.

# Example

# For xp = [200, 100, 70, 130, 100, 800, 810], the output should be
# solution(xp) = [[1, 4], [5, 6], [2, 3]].

# Initially, search ranges for users 1 and 4 (these are their IDs equal to 0-based indices) coincide, so they form the first pair.
# After 5 steps search circles of users 5 and 6 intersect. Thus, they form the second pair.
# After 25 more steps search circles of users 2 and 3 intersect. Thus, they form the third pair.
# Finally, user 0 remains without an opponent.


def solution(xp):
    # Create a list of users with their xp and id
    users = sorted([(xp[i], i) for i in range(len(xp))])
    pairs = []
    while len(users) > 1:
        # Find the pair of users with the closest xp
        min_diff = float('inf')
        pair = None
        for i in range(len(users) - 1):
            diff = users[i + 1][0] - users[i][0]
            if diff < min_diff:
                min_diff = diff
                pair = (users[i], users[i + 1])
        # Remove the pair from the list of users
        users.remove(pair[0])
        users.remove(pair[1])
        # Add the pair to the list of pairs
        pairs.append(sorted([pair[0][1], pair[1][1]]))
    return pairs

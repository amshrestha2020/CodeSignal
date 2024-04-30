# You've been walking in the woods you got so attached to for the entire day. The weather was nice and warm, the smell of the nature was wonderful, and you got so carried away (both literally and virtually) that didn't even notice when it started to get cold. Your home is too far from your current location, and you're barely standing on your feet having walked for so long, so you have no other option but to make your bed right where you are.

# Since it's really cold already, you'd like to start a campfire. Of course playing with fire is a bad idea, especially in dry woods, but you didn't sleep last night and need at least k hours of sleep to think straight the next day. You assume that if the fire starts in some meadow, each hour it'll spread to all the neighboring meadows, each of which will in turn set their neighboring meadows on fire in another hour.

# There are n meadows in the forest, and you're going to start a campfire in your current meadow start. Knowing how the meadows are connected (this information is given as a matrix wmap), find out which meadows may be on fire when you wake up after k hours and return the list of these meadows sorted in ascending order (don't worry about yourself - woods around you are not dry, so the fire in your meadow won't hurt you).

# Example

# For n = 5, wmap = [[0, 1], [1, 2], [2, 3], [3, 4], [4, 0]],
# start = 0, and k = 1, the output should be
# solution(n, wmap, start, k) = [0, 1, 4].



# For n = 7,

# wmap = [[0, 1], [1, 2], [2, 3], [3, 4], 
#          [4, 5], [5, 6], [6, 0], [4, 1]]
# start = 0, and k = 2, the output should be
# solution(n, wmap, start, k) = [0, 1, 2, 4, 5, 6].



# At the beginning of the first hour meadow 0 starts burning. At the second hour meadows 1 and 6 start burning as well. At the third hour neighbors of meadow 1 - meadows 2 and 4 - catch on fire, and so does the only neighbor of meadow 6 - meadow 5. So, at the end of the third hour meadows 0, 1, 2, 4, 5 and 6 will be on fire.


from collections import defaultdict, deque

def solution(n, wmap, start, k):
    adj = defaultdict(list)
    for i, j in wmap:
        adj[i].append(j)
        adj[j].append(i)

    visited = [False]*n
    visited[start] = True
    queue = deque([(start, 0)])
    while queue:
        node, hour = queue.popleft()
        if hour < k:
            for neighbor in adj[node]:
                if not visited[neighbor]:
                    visited[neighbor] = True
                    queue.append((neighbor, hour+1))

    return [i for i, v in enumerate(visited) if v]

# You got sick because of walking in the woods at night, and have to spend a week at home without going out. Looking out of the window at the nearby woods you're wondering if there is anything you don't yet know about them. Suddenly you see a beautiful and very tall tree you haven't seen before. Since you have nothing to do, you decide to examine its structure and draw it in your notebook.

# You became so exited about this new tree that your temperature went up, so you were forced to stay in bed. You can't see the tree from your bed, but luckily you have it drawn down. The first thing you'd like to find out about is the tree height. Looking at your drawing you suddenly realize that you forgot to mark the tree bottom and you don't know from which vertex you should start counting. Of course a tree height can be calculated as the length of the longest path in it (it is also called tree diameter). So, now you have a task you need to solve, so go ahead!

# Example

# For n = 10 and

# tree = [[2, 5], [5, 7], [5, 1], [1, 9], [1, 0], [7, 6], [6, 3], [3, 8], [8, 4]]
# the output should be solution(n, tree) = 7.



# The longest path is the path from vertex 4 to one vertex 9 or 0.


from collections import defaultdict

def dfs(v, parent, adj):
    max1 = max2 = 0
    for u in adj[v]:
        if u == parent:
            continue
        d = dfs(u, v, adj) + 1
        if d > max1:
            max1, max2 = d, max1
        elif d > max2:
            max2 = d
    dfs.diameter = max(dfs.diameter, max1 + max2)
    return max1

def solution(n, tree):
    adj = defaultdict(list)
    for i, j in tree:
        adj[i].append(j)
        adj[j].append(i)

    dfs.diameter = 0
    dfs(0, -1, adj)
    return dfs.diameter

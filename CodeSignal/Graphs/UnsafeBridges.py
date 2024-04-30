# You are the leader of a tribe living on a remote archipelago. Your tribe has recently decided to find a new, more comfortable and less remote place for everybody and moved to a new archipelago. It's a new and unexplored place that can hide many dangers, so you started off by drawing its map. You got a map of n islands and several bridges connecting them. Of course, not all the islands are necessarily connected: there may be no route from one island to another even through other islands.

# Since you're just exploring the archipelago, there are not enough bridges yet, and its connectivity is not perfect. You define the connectivity as the number of unsafe bridges on the archipelago, and call a bridge unsafe if removing it disconnects some pair of previously connected islands. More formally, an unsafe bridge is such a bridge that removing it increases the number of pairs of islands (v, u) such that u is unreachable from v.

# You decided to build some new bridges to connect more islands of your new home. To begin with, you drew a plan containing a list of newBridges that you're going to build in the exact given order. Since you're short of resources after all the moving, you'd like to make sure that building each new bridge is really necessary. Given the number of islands n and the existing bridges, find the sum of connectivities of the archipelago after building each bridge from newBridges consequentially modulo 109 + 7 (hopefully this value will be descriptive enough).

# Example

# For n = 6, bridges = [[0, 1], [1, 2], [2, 3], [3, 4], [4, 5]], and
# newBridges = [[2, 4], [1, 3], [3, 5], [0, 5]], the output should be
# solution(n, bridges, newBridges) = 6.

# After building the 1st bridge connectivity will be equal to 3;
# After building the 2nd bridge connectivity will be equal to 2;
# After building the 3rd bridge connectivity will be equal to 1;
# After building the 4th bridge connectivity will be equal to 0.
# So, the summary connectivity is 3 + 2 + 1 + 0 = 6.


import numpy as np

def solution(n, bridges, newBridges):
    par = [-1] * n 
    dsu_2ecc = np.arange(n)
    dsu_cc = np.arange(n)
    dsu_cc_size = [1] * n 
    last = [0] * n
    global lca_iteration, bridge
    bridge = lca_iteration = 0
    
    def find_2ecc(v):
        if v == -1:
            return -1
        while dsu_2ecc[v] != v:
            v = dsu_2ecc[v]
        return v    
    
    def find_cc(v):
        v = find_2ecc(v)
        while dsu_cc[v] != v:
            v = dsu_cc[v]
        return v 
    
    def make_root(v):
        v = find_2ecc(v)
        root = v;
        child = -1
        while v != -1: 
            p = find_2ecc(par[v])
            par[v] = child
            dsu_cc[v] = root
            child = v
            v = p
        dsu_cc_size[root] = dsu_cc_size[child]
    
    def merge_path(a, b):
        global lca_iteration, bridge
        lca_iteration += 1
        path_a = []
        path_b = []
        lca = -1
        while lca == -1:
            if a != -1:
                a = find_2ecc(a)
                path_a.append(a);
                if last[a] == lca_iteration:
                    lca = a
                else:
                    last[a] = lca_iteration 
                a = par[a]
            if b != -1:
                b = find_2ecc(b)
                path_b.append(b)
                if last[b] == lca_iteration:
                    lca = b
                else:
                    last[b] = lca_iteration 
                b = par[b]
        for v in path_a:
            dsu_2ecc[v] = lca
            if v == lca:
                break
            bridge -= 1
        for v in path_b:
            dsu_2ecc[v] = lca
            if v == lca:
                break
            bridge -= 1
    
    def add_edge(a, b):
        global bridge
        a = find_2ecc(a)
        b = find_2ecc(b)
        if a != b:
            ca = find_cc(a)
            cb = find_cc(b)
            if ca != cb:
                bridge += 1
                if dsu_cc_size[ca] > dsu_cc_size[cb]:
                    a, b = b, a
                    ca, cb = cb, ca
                make_root(a)
                par[a] = dsu_cc[a] = b
                dsu_cc_size[cb] += dsu_cc_size[a]
            else:
                merge_path(a, b)
    
    s = 0
    for x, y in bridges:
        add_edge(x, y)
    for x, y in newBridges:
        add_edge(x, y)
        s += bridge 
    
    return s % (10 ** 9 + 7)

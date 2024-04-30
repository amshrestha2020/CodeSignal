# You're working in a big delivery company that has to handle a lot of orders on a daily basis. To optimize the delivery process your boss gave you a plan of the city containing n buildings and some streets connecting them, and asked to build an optimal delivery plan for the couriers. The plan should contain several streets connecting all the buildings in such way that each building is reachable from any other one, and should have the minimum total length of all the streets in it among all possible plans.

# Since this task is too simple for you, you'd like to make it a bit more challenging. You know that using the same delivery plan every time is boring for many couriers, so you'd like to find all possible different optimal plans. To begin with, you'd like to calculate the number of such plans for the given n and streets. Since this number can be very big, return it modulo 109 + 7.

# Example

# For n = 4 and streets = [[0, 1, 1], [0, 3, 2], [1, 2, 2], [2, 3, 2]],
# the output should be
# solution(n, streets) = 3.



# There are 3 possible optimal delivery plans with the total streets length equal to 5:

# 0 -- 1, 0 -- 3, 1 -- 2;
# 0 -- 1, 1 -- 2, 2 -- 3;
# 0 -- 1, 0 -- 3, 2 -- 3.

from math import gcd
from collections import defaultdict

def solution(n, streets):
    MOD = 10 ** 9 + 7

    def simp(a, b):
        d = gcd(a, b)
        return a // d, b // d

    def msts(A):
        n = len(A) - 1
        B = [[1]*n for _ in range(n)]
        for k in range(n - 1):
            for i in range(k + 1, n):
                for j in range(k + 1, n):
                    xa, xb = simp(A[k][k] * A[i][j], B[k][k] * B[i][j])
                    ya, yb = simp(A[i][k] * A[k][j], B[i][k] * B[k][j])
                    da, db = (A[k - 1][k - 1], B[k - 1][k - 1]) if k > 0 else (1, 1)
                    A[i][j], B[i][j] = simp(db*(xa*yb - ya*xb), da*xb*yb)
        return A[n - 1][n - 1] // B[n - 1][n - 1]

    clist = {i: {i} for i in range(n)}
    cmap = {i: i for i in range(n)}
    adj = [set() for _ in range(n)]
    smap = defaultdict(set)
    for s in streets:
        adj[s[0]].add(s[1])
        adj[s[1]].add(s[0])
        smap[s[2]].add((s[0], s[1]))

    res = 1
    for cost in sorted(smap):
        plist = {i: {i} for i in clist}
        pmap = {i: i for i in clist}
        for s in smap[cost]:
            p0, p1 = pmap[cmap[s[0]]], pmap[cmap[s[1]]]
            if p0 != p1:
                for c in plist[p1]:
                    pmap[c] = p0
                    plist[p0].add(c)
                del plist[p1]

        for p in plist:
            if len(plist[p]) > 1:
                L = [[0]*len(plist[p]) for _ in range(len(plist[p]))]
                l = {v: i for i, v in enumerate(sorted(plist[p]))}
                for s in smap[cost]:
                    c0, c1 = cmap[s[0]], cmap[s[1]]
                    if c0 != c1 and pmap[c0] == p and pmap[c1] == p:
                        L[l[c0]][l[c0]] += 1
                        L[l[c1]][l[c1]] += 1
                        L[l[c0]][l[c1]] -= 1
                        L[l[c1]][l[c0]] -= 1
                res = (res * (msts(L) % MOD)) % MOD

        clist2 = {p: set() for p in plist}
        cmap2 = {}
        for p in plist:
            for c in plist[p]:
                for v in clist[c]:
                    clist2[p].add(v)
                    cmap2[v] = p

        clist = clist2
        cmap = cmap2

    return res

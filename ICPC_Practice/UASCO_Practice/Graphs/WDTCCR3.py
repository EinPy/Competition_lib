#solution to http://www.usaco.org/index.php?page=viewproblem2&cpid=716

import sys
from collections import *
sys.setrecursionlimit(10**5)
itr = (line for line in sys.stdin.read().strip().split('\n'))
INP = lambda: next(itr)
def ni(): return int(INP())
def nl(): return [int(_) for _ in INP().split()]



n, k, r = nl()
g = [[-1 for _ in range(n)] for _ in range(n)]
for _ in range(r):
    rs,cs,re,ce = nl()
    rs -= 1
    cs -= 1
    re -= 1
    ce -= 1
    r1 = min(rs, re)
    r2 = max(rs, re)
    c1 = min(cs, ce)
    c2 = max(cs,ce)
    print(r1, c1, r2, c2)
    if r1 == r2:
        for i in range(c1, c2 + 1):
            print(i)
            g[r1][i] = "#"
    if c1 == c2:
        for i in range(r1, r2 + 1):
            g[i][c1] = "#"

for l in g: print(l)
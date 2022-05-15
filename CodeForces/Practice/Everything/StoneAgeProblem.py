import sys
from collections import *
sys.setrecursionlimit(10**5)
itr = (line for line in sys.stdin.read().strip().split('\n'))
INP = lambda: next(itr)
def ni(): return int(INP())
def nl(): return [int(_) for _ in INP().split()]




n,q = nl()
a = nl()
tot = sum(a)
for _ in range(q):
    que = nl()
    t, i, x = 0,0,0
    if que[0] == 1:
        i, x = que[1], que[2]
        tot += x - a[i-1]
        a[i-1] = x
    if que[0] == 2:
        x = que[1]
        tot = x * n
        a = [x for _ in range(n)]
    print(tot)
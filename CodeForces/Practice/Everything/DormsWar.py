import sys
from collections import *
sys.setrecursionlimit(10**5)
itr = (line for line in sys.stdin.read().strip().split('\n'))
INP = lambda: next(itr)
def ni(): return int(INP())
def nl(): return [int(_) for _ in INP().split()]




def solve(n,s,k):
    k = k.split()
    nk = k[0]
    k.pop(0)

    for i in range(n):
        if s[i] in k:
            dist = i
            return dist

#oel


t = ni()
for _ in range(t):
    n = ni()
    s = INP()
    k = INP()
    solve(n,s,k)
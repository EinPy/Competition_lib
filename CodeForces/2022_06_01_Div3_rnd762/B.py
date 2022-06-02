import sys
from collections import *
sys.setrecursionlimit(10**5)
itr = (line for line in sys.stdin.read().strip().split('\n'))
INP = lambda: next(itr)
def ni(): return int(INP())
def nl(): return [int(_) for _ in INP().split()]


import math
def solve(n):
    seen = {}
    #print(int(math.floor(math.sqrt(n))) + 1)
    #print(low)
    for i in range(1,int(math.floor(math.sqrt(n)))+ 1):
        a, b = i ** 2, i ** 3
        #print(i)
        if a not in seen:
            seen[a] = True
        if b <= n and b not in seen:
            seen[b] = True
    #print()
    print(len(seen.keys()))


t = ni()
for case in range(t):
    n = ni()
    solve(n)
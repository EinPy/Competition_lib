#solution to https://cses.fi/problemset/task/1652
import sys
from collections import *
sys.setrecursionlimit(10**5)
itr = (line for line in sys.stdin.read().strip().split('\n'))
INP = lambda: next(itr)
def ni(): return int(INP())
def nl(): return [int(_) for _ in INP().split()]


n, q = nl()
#padded with zeroes on left and top due to 1 indexation
pref = [[0 for _ in range(n+1)] for _ in range(n+1)]
for line in range(1,n+1):
    l = list(INP())
    for i, s in enumerate(l):
        ii = i + 1
        pref[line][ii] = pref[line-1][ii] + pref[line][ii-1] - pref[line-1][ii-1]
        if s == '*': 
            pref[line][ii] += 1
        
#for r in pref:print(r)
for i in range(q):
    y1, x1, y2, x2 = nl()
    tot = pref[y2][x2] - pref[y2][x1-1] - pref[y1-1][x2] + pref[y1-1][x1-1]
    print(tot)
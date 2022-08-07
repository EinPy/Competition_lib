#https://codeforces.com/contest/1325/problem/C

import sys
from collections import *
sys.setrecursionlimit(10**5)
itr = (line for line in sys.stdin.read().strip().split('\n'))
INP = lambda: next(itr)
def ni(): return int(INP())
def nl(): return [int(_) for _ in INP().split()]



def solve(n, g, edge):
    visited = [False for _ in range(n+1)]
    triplets = {}
    pos = False
    for i in range(1,n+1):
        if len(g[i]) >= 3:
            pos = True
            for j in range(3):
                triplets[g[i][j][1]] = True
            break
    cnt = 0
    cnt2 = 3
    if pos:
        for i in range(n-1):
            if i in triplets:
                print(cnt)
                cnt += 1
            else:
                print(cnt2)
                cnt2 += 1
    else:
        for i in range(n-1):
            print(i)
    

n = ni()
g = [[] for _ in range(n+1)]
edge = []
for nr in range(n-1):
    a, b = nl()
    g[a].append((b,nr))
    g[b].append((a, nr))
    edge.append((a,b))
    
solve(n, g, edge)
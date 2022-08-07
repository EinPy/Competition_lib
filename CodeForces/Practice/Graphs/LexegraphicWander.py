#https://codeforces.com/problemset/problem/1106/D
import heapq
import sys
from collections import *
sys.setrecursionlimit(10**5)
itr = (line for line in sys.stdin.read().strip().split('\n'))
INP = lambda: next(itr)
def ni(): return int(INP())
def nl(): return [int(_) for _ in INP().split()]


n, m = nl()
g = [[] for _ in range(n+1)]
for _ in range(m):
    a, b = nl()
    g[a].append(b)
    g[b].append(a)
    
vis = [False for _ in range(n+1)]

vis[1] = True
q = []
heapq.heappush(q, 1)
#print(q)

#print(q)
while q:
    node = heapq.heappop(q)
    print(node, end = " ")
    for v in g[node]:
        if not vis[v]:
            heapq.heappush(q, v)
            vis[v] = True
    

#solution toL: https://cses.fi/problemset/task/1666
import sys
from collections import *
sys.setrecursionlimit(10**5)
itr = (line for line in sys.stdin.read().strip().split('\n'))
INP = lambda: next(itr)
def ni(): return int(INP())
def nl(): return [int(_) for _ in INP().split()]



def solve(n,a):
    pass



n, m = nl()
adj = [[] for _ in range(n+1)]
vis = [False] * (n+1)
for i in range(m):
    a, b = nl()
    adj[a].append(b)
    adj[b].append(a)


def dfs(s,g):
    q = [s]
    while q:
        n = q.pop()
        for v in adj[n]:
            if not vis[v]:
                vis[v] = True
                q.append(v)


comp = 0
add = []
for i in range(1, n+1):
    if not vis[i]:
        add.append(i)
        dfs(i,adj)
        comp += 1
        
print(comp - 1)
if comp -1 > 0:
    for r in range(1,len(add)):
        print(add[0], add[r])
        
#solution to https://cses.fi/problemset/task/1666
import sys
from collections import *
sys.setrecursionlimit(10**5)
itr = (line for line in sys.stdin.read().strip().split('\n'))
INP = lambda: next(itr)
def ni(): return int(INP())
def nl(): return [int(_) for _ in INP().split()]


#keep track of where all dfs were started
#When one dfs runs out you start a new one and add a new node to started


def solve(n,adj, rev):
    vis = [False for _ in range(n+1)]
    vis[0] = True
    
    def dfs(start):
        q = deque([start])
        vis[start] = True
        while q:
            n = q.popleft()
            for v in adj[n]:
                if not vis[v]:
                    q.append(v)
                    vis[v] = True
                    
    starts = []
    for v in range(n+1):
        if not vis[v]:
            dfs(v)
            starts.append(v)
    print(len(starts)-1)
    for i in range(1,len(starts)):
        print(starts[0], starts[i])
            
        



t, m = nl()
adj, rev = [[] for _ in range(t+1)], [[] for _ in range(t+1)]
for r in range(m):
    a, b = nl()
    adj[a].append(b)
    adj[b].append(a)
    
solve(t, adj, rev)
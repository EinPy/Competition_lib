#solution to https://cses.fi/problemset/task/1682
import sys
from collections import *
sys.setrecursionlimit(10**5)
itr = (line for line in sys.stdin.read().strip().split('\n'))
INP = lambda: next(itr)
def ni(): return int(INP())
def nl(): return [int(_) for _ in INP().split()]



def solve(n,adj, rev):
    vis = [False for _ in range(n+1)]
    vis[0] = True
    
    def dfs(s):
        q = deque([s])
        order = []
        vis[s] = True
        while q:
            cur = q.pop()
            print(cur)
            order.append(cur)
            for n in adj[cur]:
                if not vis[n]:
                    q.append(n)
                    vis[n] = True
        return order[::-1]
    
    ord = []
    for i in range(n+1):
        if not vis[i]:
            ord.append(dfs(i))
    


n, c = nl()
adj = [[] for _ in range(n+1)]
rev = [[] for _ in range(n+1)]
#print(adj)
for _ in range(c):
    a, b = nl()
    #print(a,b)
    adj[a].append(b)
    rev[b].append(a)
solve(n, adj, rev)  
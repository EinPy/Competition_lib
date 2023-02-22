import sys
from collections import *
sys.setrecursionlimit(10**5)
itr = (line for line in sys.stdin.read().strip().split('\n'))
INP = lambda: next(itr)
def ni(): return int(INP())
def nl(): return [int(_) for _ in INP().split()]

adj, adj_rev = [], []
used =[]
order, component = [],[]
N = 0

def dfs1(v):
    #print(used)
    used[v] = True
    for u in adj[v]:
        if not used[u]:
            dfs1(u)
    order.append(v)
    
def dfs2(v):
    used[v] = True
    component.append(v)
    for u in adj_rev[v]:
        if not used[u]:
            dfs2(u)
    
    
N, T = nl()

adj = [[] for _ in range(N)]
adj_rev = [[] for _ in range(N)]

for case in range(T):
    a,b = nl()
    a -= 1
    b -= 1
    adj[a].append(b)
    adj[b].append(a)
    #fix lists


c = 0
used = [False] * N

for i in range(0, N):
    if not used[i]:
        dfs1(i)
        
print(used)
print(order)
used = [False] * N


order.reverse()
print(order)

for n in order:
    if not used[n]:
        c += 1
        dfs2(n)
        #processing component
        component = []
print(c)
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

def dfs1(v):
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

def solve(n,a):
    used = [False] * N
    
    for i in range(0, N):
        if not used[i]:
            dfs1(i)
            
    used = [False] * N
    
    order.reverse()
    
    for n in order:
        if not used[n]:
            dfs2(n)
            #processing component

            component = []

    roots = []
    root_nodes = []
    adj_scc = [[]]
    
    for v in order:
        if not used[v]:
            dfs2(v)
            
            root = component[0]
            for u in component:
                roots[u] == root
            component = []
            
    for v in range(0,N):
        for u in adj[v]:
            root_v = roots[v]
            root_u = roots[]
            
            if root_u != root_v:
                adj_scc[root_v].append(root_u)
t = ni()
for case in range(t):
    a, b = nl()
    #fix lists
import sys
from collections import *
sys.setrecursionlimit(10**5)
itr = (line for line in sys.stdin.read().strip().split('\n'))
INP = lambda: next(itr)
def ni(): return int(INP())
def nl(): return [int(_) for _ in INP().split()]



def kosa(adj, adj_rev):
    n = len(adj)
    sccs = []
    part_of = [0] * n
    
    stack = []
    visited = [False] * n
    
    #steg 1
    def dfs1(node):
        if visited[node]:
            return
        visited[node] = True
        for u in adj[node]:
            dfs1(u)
        stack.append(node)
        
        
    for node in range(n):
        dfs1(node)
    #print(visited)
    
    visited = [False] * n
    def dfs2(node):
        visited[node] = True
        sccs[-1].append(node)
        part_of[node] = len(sccs) - 1
        for u in adj_rev[node]:
            if not visited[u]:
                dfs2(u)
                
    
    biggest = 0
    for node in reversed(stack):
        if not visited[node]:
            cur = 0
            sccs.append([])
            dfs2(node)
            cur = len(sccs[-1])
            #print(sccs)
            biggest = max(cur,biggest)
    #print(biggest)
    return (sccs, part_of, len(sccs) == n, biggest)


N = ni()

adj = [[] for _ in range(N)]
adj_rev = [[] for _ in range(N)]
understands = []
speaks = []
for case in range(N):
    L = INP().split()
    d = {}
    speaks.append(L[1])
    for u in L[1:]:
        d[u] = True
    understands.append(d)
#print(speaks)
#print(understands)
for i in range(N):
    for j in range(N):
        if i != j:
            if speaks[i] in understands[j]:
                adj[i].append(j)
                adj_rev[j].append(i)
#print(adj)
#print(adj_rev)

sccs, part, trash, biggest = kosa(adj, adj_rev)
#print(biggest)
print(N - biggest)

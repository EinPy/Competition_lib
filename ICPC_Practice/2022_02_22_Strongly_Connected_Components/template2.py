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
                
    
            
    for node in reversed(stack):
        if not visited[node]:
            sccs.append([])
            dfs2(node)
            
    return (sccs, part_of, len(sccs) == n)


N, T = nl()

adj = [[] for _ in range(N)]
adj_rev = [[] for _ in range(N)]

for case in range(T):
    a,b = nl()
    a -= 1
    b -= 1
    adj[a].append(b)
    adj_rev[b].append(a)

# print(adj)
# print(adj_rev)
# print(kosa(adj, adj_rev))
sccs, part, trash = kosa(adj, adj_rev)
print(len(sccs))
out = []
for p in part:
    out.append(p + 1)
print(' '.join(map(str, out)))
# succ = []
# (sccs, part_of, _) = kosa(adj, adj_rev)
# l = len(sccs)
# dp = [1] * l
# total = 1
# MOD = int(1e9) + 7
# for scc in sccs:
#     if len(scc) > 1:
#         node = scc[0]
#         index = part_of[node]
#         total = (total * (dp[index] + 1)) % MOD
#     else:
#         node = scc[0]
#         scc_node = part_of[node]
#         s = succ[node]
#         scc_s = part_of[s]
        
import sys
from collections import *
sys.setrecursionlimit(10**5)
itr = (line for line in sys.stdin.read().strip().split('\n'))
INP = lambda: next(itr)
def ni(): return int(INP())
def nl(): return [int(_) for _ in INP().split()]



def kosaraju(adj):
    n = len(adj)
    scc = []
    part_of = [0] * n
    stack = []

    def dfs(adj, order, first_iteration):
        visited = [False] * n
        dfs_stack = []
        for node in order:
            if not visited[node]:
                visited[node] = True
                dfs_stack.append((node, 0))
                if not first_iteration:
                    scc.append([])
                while dfs_stack:
                    (node, next) = dfs_stack.pop()
                    visited[node] = True
                    if next == len(adj[node]):
                        if first_iteration:
                            stack.append(node)
                        else:
                            part_of[node] = len(scc) - 1
                            scc[-1].append(node)
                    else:
                        dfs_stack.append((node, next + 1))
                        if not visited[adj[node][next]]:
                            dfs_stack.append((adj[node][next], 0))

    dfs(adj, range(n), True)

    adj_rev = [[] for _ in range(n)]
    for (a, adj) in enumerate(adj):
        for b in adj:
            adj_rev[b].append(a)

    dfs(adj_rev, reversed(stack), False)

    is_dag = n == len(scc)
    return (scc, part_of, is_dag)


cases = ni()
for c in range(cases):
    N, T = nl()
 
    adj = [[] for _ in range(N)]
    adj_rev = [[] for _ in range(N)]

    for row in range(T):
        a,b = nl()
        a -= 1
        b -= 1
        adj[a].append(b)
        adj_rev[b].append(a)
    
    sccs, part, trash = kosaraju(adj)

    in_deg = [0 for _ in range(len(sccs))]
    for node in range(N):
        for neigh in adj[node]:
            if in_deg[part[neigh]] == 0 and part[node] != part[neigh]:
                #cond[part[node]].append(part[neigh])
                #cond_rev[part[neigh]]
                in_deg[part[neigh]] += 1
                
    cnt = 0
    for ind in in_deg:
        if ind == 0:
            cnt += 1
    print(cnt)

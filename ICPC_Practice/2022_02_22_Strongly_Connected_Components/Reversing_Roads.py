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

cnt = 1
while True:
    try:
        #print("start")
        N, R = nl()
        case = []
        for _ in range(R):
            a,b = nl()
            case.append([a,b])
        
        #print(case)
        
        adj = [[] for _ in range(N)]
        adj_rev = [[] for _ in range(N)]
        #print(adj)
        for i in range(len(case)):
            a,b = case[i][0], case[i][1]

            adj[a].append(b)
            adj_rev[b].append(a)

        #print(adj, adj_rev)
        sccs, part, trash = kosa(adj, adj_rev)
        if len(sccs) == 1:
            print(f"case {cnt}: valid")
        else:
            val = False
            for rev in range(len(case)):
                adj = [[] for _ in range(N)]
                adj_rev = [[] for _ in range(N)]

                for i in range(len(case)):
                    a,b = case[i][0], case[i][1]
                    if i != rev:
                        adj[a].append(b)
                        adj_rev[b].append(a)
                    else:
                        adj[b].append(a)
                        adj_rev[a].append(b)

                sccs, part, trash = kosa(adj, adj_rev)
                if len(sccs) == 1:
                    if not val:
                        val = True
                        print(f"case {cnt}: {case[rev][0]} {case[rev][1]}")
            if not val:
                print(f"case {cnt}: invalid")
        cnt += 1
    except:
        exit()

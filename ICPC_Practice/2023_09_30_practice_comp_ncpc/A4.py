import sys
from collections import *
sys.setrecursionlimit(10**5)
itr = (line for line in sys.stdin.read().strip().split('\n'))
INP = lambda: next(itr)
def ni(): return int(INP())
def nl(): return [int(_) for _ in INP().split()]



A, B, E, P = nl()

#A, B interval
adj = [[] for _ in range(E)]
adjRev = [[] for _ in range(E)]


#E Employe, P edges
for _ in range(P):
    a, b = nl()
    adj[a].append(b)
    adjRev[b].append(a)
    
print(adj)
    

#Bfs to find count of chilren
def bfs(Graph, S):
    q = [S]
    vis = [False for _ in range(len(Graph))]
    vis[S] = True
    children = 0
    while q:
        q2 = []
        for u in q:
            print("visiting", u)
            for n in Graph[u]:
                if not vis[n]:
                    vis[n] = True
                    children += 1
                    q2.append(n)
    return children

print(adj)
#print(bfs(adj, 0))
# succ = [bfs(adj, i) for i in range(E)]
# pred = [bfs(adjRev, i) for i in range(E)]

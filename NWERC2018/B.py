import sys
from collections import *
sys.setrecursionlimit(10**5)
itr = (line for line in sys.stdin.read().strip().split('\n'))
INP = lambda: next(itr)
def ni(): return int(INP())
def nl(): return [int(_) for _ in INP().split()]



def bfs(adj, s, vis):
    q = [s]
    vis[s] = True
    cnt = 0
    while q:
        q2 = []
        for u in q:
            for v in adj[u]:
                ifgo_back = True
        q = q2
    return vis, cnt
                    


n = ni()
T = [[-1,-1] for _ in range(n)]
adj = [[] for _ in range(n)]
for i in range(n):
    l = nl()
    m = l[0]
    dep = l[1]
    T[i][0] = m
    T[i][1] = i
    for j in range(2, len(l)):
        adj[i].append(l[j]-1)
        
T.sort(reverse=True)
vis = [False for _ in range(n)]
t = 0
#print(T)
maxT = 0

for time, node in T:
    if not vis[node]:
        vis, cnt = bfs(adj, node, vis)
        t += cnt
        maxT = max(maxT,time + t)
        t += 1
print(maxT)

#
#
#
#LRDUL
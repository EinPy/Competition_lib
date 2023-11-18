

import sys
from collections import *
sys.setrecursionlimit(10**5)
itr = (line for line in sys.stdin.read().strip().split('\n'))
INP = lambda: next(itr)
def ni(): return int(INP())
def nl(): return [int(_) for _ in INP().split()]

N, M = nl()


adj = [[] for _ in range(N)]
vis = [False for _ in range(N)]
tin = [-1 for _ in range(N)]
low = [-1 for _ in range(N)]
global timer
timer = 0 #keep track if time in, discorvery order
bridges = []

def dfs(v, p = -1):
    global timer
    vis[v] = True
    timer += 1
    tin[v] = timer
    low[v] = timer
    for to in adj[v]:
        if to == p:
            continue
        if vis[to]:
            low[v] = min(low[v], tin[to])
        else:
            dfs(to, v)
            low[v] = min(low[v], low[to])
            if low[to] > tin[v]:
                bridges.append((v, to))
            
#find nodes on other side of bridge

global cnt
cnt = 0
def find(v, dont):
    #print(f"visiting {v}")
    global cnt
    cnt += 1
    vis [v] = True
    for u in adj[v]:
        if not vis[u] and u != dont:
            find(u, dont)
    

for _ in range(M):
    a, b = nl()
    adj[a].append(b)
    adj[b].append(a)
    

    
dfs(0)
vis = [False for _ in range(N)]
#print(bridges)

for (fr, to) in bridges:
    find(to, fr)
#print(len(bridges))
print(N -cnt)


import sys
from collections import *
sys.setrecursionlimit(10**5)
itr = (line for line in sys.stdin.read().strip().split('\n'))
INP = lambda: next(itr)
def ni(): return int(INP())
def nl(): return [int(_) for _ in INP().split()]



adj = [[] for _ in range(100)]
vis = [False for _ in range(100)]
tin = [-1 for _ in range(100)]
low = [-1 for _ in range(100)]
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
            
p, c = nl()
while True:
    adj = [[] for _ in range(p)]
    vis = [False for _ in range(p)]
    tin = [-1 for _ in range(p)]
    low = [-1 for _ in range(p)]
    timer = 0 #keep track if time in, discorvery order
    bridges = []
    for pair in range(c):
        a, b = nl()
        adj[a].append(b)
        adj[b].append(a)
    for i in range(p):
        if not vis[i]:
            dfs(i)
    if len(bridges) != 0:
        print("Yes")
    else:
        print("No")

    p, c = nl()
    if p == 0 and c == 0:
        break
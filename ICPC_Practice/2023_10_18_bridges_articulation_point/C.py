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
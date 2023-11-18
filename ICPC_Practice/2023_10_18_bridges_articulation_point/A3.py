import sys
from collections import *
sys.setrecursionlimit(10**5)
itr = (line for line in sys.stdin.read().strip().split('\n'))
INP = lambda: next(itr)
def ni(): return int(INP())
def nl(): return [int(_) for _ in INP().split()]


vis = [False for _ in range(100)]
G = [[] for _ in range(100)]
dfsT = [[] for _ in range(100)]
back_edge = [[] for _ in range(100)]
back_edge_rev = [[] for _ in range(100)]
dp = [False for _ in range(100)]
global found_back_edge
found_back_edge = False

def dfs(u, parent):
    vis[u] = True
    for n in G[u]:
        if not vis[n]:
            vis[n] = True
            dfsT[u].append(n)
            dfs(n, u)
        else:
            if parent != -1 and n != parent:
                back_edge[u].append(n)

def visit(u):
    #print(f"visiting {u}")
    dp[u] += len(back_edge[u])
    dp[u] -= len(back_edge_rev[u])
    global found_back_edge
    for v in dfsT[u]:
        if dp[v] != False:
            dp[u] += dp[v]
        else:
            dp[u] += visit(v)
    if dp[u] == 0:
        #print(u)
        found_back_edge = True
    #print(f"node {u} has dp {dp[u]}")
    return dp[u]


p, c = nl()
while True:
    vis = [False for _ in range(p)]
    G = [[] for _ in range(p)]
    dfsT = [[] for _ in range(p)]
    back_edge = [[] for _ in range(p)]
    back_edge_rev = [[] for _ in range(p)]
    dp = [False for _ in range(p)]
    for pair in range(c):
        a, b = nl()
        G[a].append(b)
        G[b].append(a)
    if p == 1:
        print("No")
    elif p == 2:
        print("Yes")
    else:     
        dfs(0, -1)
        visit(0)
        if found_back_edge:
            print("Yes")
        else:
            print("No")
    found_bridge = False

    p, c = nl()
    if p == 0 and c == 0:
        break
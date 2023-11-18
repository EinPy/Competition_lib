import sys
from collections import *
sys.setrecursionlimit(10**5)
itr = (line for line in sys.stdin.read().strip().split('\n'))
INP = lambda: next(itr)
def ni(): return int(INP())
def nl(): return [int(_) for _ in INP().split()]


vis = [False for _ in range(100)]
height = [-1] * 100
G = [[] for _ in range(100)]
dfsT = [[] for _ in range(100)]
back_edge = [[] for _ in range(100)]
min_reach = [1e9 for _ in range(100)]
global found_bridge
gound_bridge = False

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
            
#Bfs to find distannce to all nodes in graph, damn this could be done in the dfs
 
def bfs(Graph, S):
    q = [S]
    while q:
        q2 = []
        for u in q:
            for n in dfsT[u]:
                if height[n] == -1:
                    height[n] = height[u] + 1
                    q2.append(n)
        q = q2
    return height
#idea is to check if any of you children an reach a node above yourself

def find(u):
    #print(f"visiting {u}")
    vis[u] = True
    reachable_min = 1e9
    global found_bridge
    for n in dfsT[u]:
        if not vis[n]:
            reachable_min = min(find(n), reachable_min)
    if len(dfsT[u]) != 0 and reachable_min > height[u]:
        #print(f"at {u} child can reach {reachable_min}")
        found_bridge = True
        #print(found_bridge)
    for b in back_edge[u]:
        if height[b] < height[u]:
            reachable_min = min(reachable_min, height[b])
    min_reach[u] = reachable_min
    #print(f"node {u} can reach {min_reach[u]}")
    return min_reach[u]
        



p, c = nl()
while True:
    vis = [False for _ in range(p)]
    height = [-1] * p
    G = [[] for _ in range(p)]
    dfsT = [[] for _ in range(p)]
    back_edge = [[] for _ in range(p)]
    min_reach = [1e9 for _ in range(p)]
    for pair in range(c):
        a, b = nl()
        G[a].append(b)
        G[b].append(a)
    if p == 1:
        print("No")
    elif p == 2:
        print("Yes")
    else:     
        height[0] = 0
        dfs(0, -1)
        bfs(G,0)
        #print(dfsT)
        #print(height)
        #print(back_edge)
        vis = [False for _ in range(p)]
        find(0)
        if found_bridge:
            print("Yes")
        else:
            print("No")
    found_bridge = False

    p, c = nl()
    if p == 0 and c == 0:
        break
    

            
            
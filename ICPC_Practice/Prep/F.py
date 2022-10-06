from operator import truediv
import sys
from collections import *
sys.setrecursionlimit(10**5)
itr = (line for line in sys.stdin.read().strip().split('\n'))
INP = lambda: next(itr)
def ni(): return int(INP())
def nl(): return [int(_) for _ in INP().split()]



air, r = nl()
g = [[] for _ in range(air+1)]
l = [-1 for _ in range(air+1)]
possible = True

add = 0
vis = [False for _ in range(air+1)]

for _ in range(r):
    a, b, c = nl()
    
    if c == 2:
        if l[a] == 0 or l[b] == 0:
            possible = False
            break
        l[a] = 1
        l[b] = 1
        if not vis[a]:
            add += 1
        if not vis[b]:
            add += 1
        vis[a] = True
        vis[b] = True
    elif c == 0:
        if l[a] == 1 or l[b] == 1:
            possible = False
            break
        l[a] = 0
        l[b] = 0
        vis[a] = True
        vis[b] = True
    else:
        g[a].append(b)
        g[b].append(a)
        

color = [-1 for _ in range(air+1)]

#print(l)
def bfs(Graph, S):
    global possible
    q = [S]
    adding = False
    Atype = -1
    A, B = 0, 0
    A = 1
    color[s] = "A"
    while q:
        q2 = []
        adding = not adding
        for u in q:
            for n in Graph[u]:
                #print(u, n, color[u], color[n])
                if color[u] != -1 and color[n] != -1:
                    if color[u] == color[n]:
                        return -1
                if not vis[n]:
                    vis[n] = True
                    q2.append(n)
                    if adding:
                        B += 1
                        color[n] = "B"
                    else:
                        A += 1
                        color[n] = "A"
                if l[n] == 0:
                    if adding:
                        if Atype == 0:
                            return -1
                        Atype = 1
                    else:
                        if Atype == 1:
                            return -1
                        Atype = 0
                if l[n] == 1:
                    if adding:
                        if Atype == 1:
                            return -1
                        Atype = 0
                    else:
                        if Atype == 0:
                            return -1
                        Atype = 1
                #print(u, n, color[u], color[n])
        q = q2
    #print(A, B, Atype)
    if Atype == 1:
        return A
    elif Atype == 0:
        return B
    else:
        return min(A,B)

for s in range(1,air+1):
    if not vis[s]:
        ans = bfs(g,s)
        if ans == -1:
            possible = False
            break
        else:
            add += ans
        
if possible:
    print(add)
else:
    print("impossible")
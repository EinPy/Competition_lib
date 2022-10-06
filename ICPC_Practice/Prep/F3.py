import sys
from collections import *
sys.setrecursionlimit(10**5)
itr = (line for line in sys.stdin.read().strip().split('\n'))
INP = lambda: next(itr)
def ni(): return int(INP())
def nl(): return [int(_) for _ in INP().split()]


a, r = nl()
g = [[] for _ in range(a+1)]
l = [-1 for _ in range(a+1)]
l1 = [-1 for _ in range(a+1)]
starts = [0 for _ in range(a+1)]
vis = [False for _ in range(a+1)]
add = 0

possible = True

for _ in range(r):
    a, b, s = nl()
    if s == 0:
        if l[a] == -1 or l[a] == 0:
            l[a] = 0
        else:
            possible = False
        if l[b] == -1 or l[b] == 0:
            l[b] = 0
        else:
            possible = False
        starts[a]= True
        starts[b] = True
    if s == 2:
        if l[a] == -1 or l[a] == 2:
            l[a] = 2
        else:
            possible = False
        if l[b] == -1 or l[b] == 2:
            l[b] = 2
        else:
            possible = False
        starts[a] = True
        starts[b] = True
    if s == 1:
        g[a].append(b)
        g[b].append(a)
        l1[a] = 1
        l1[b] = 1
        
        
        
#Bfs to find distannce to all nodes in graph 
def bfs(s):
    t = l[s]
    if t == 0:
        t = False
    if t == 2:
        t = True
    q = [s]
    vis[s] = True
    while q:
        q2 = []
        for u in q:
            for n in g[u]:
                if vis[n] == False:
                    vis[n] = True
                    q2.append(n)
        q = q2
        
for i in range(a+1):
    if starts[i]:
        bfs(i)
        
for i in range(a+1):
    if not vis[i]:
        ans = min(bfs(i, 0), bfs(i,1))
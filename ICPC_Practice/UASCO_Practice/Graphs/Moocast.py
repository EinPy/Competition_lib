#solution to http://www.usaco.org/index.php?page=viewproblem2&cpid=668
import sys
from collections import *
sys.setrecursionlimit(10**5)
sys.stdin = open("moocast.in", 'r')
sys.stdout = open("moocast.out", 'w')
itr = (line for line in sys.stdin.read().strip().split('\n'))
INP = lambda: next(itr)
def ni(): return int(INP())
def nl(): return [int(_) for _ in INP().split()]

import math

def solve(n, adj):
    
    def dfs(s):
        vis = [False] * n
        vis[s] = True
        size = 1
        q = [s]
        while q:
            v = q.pop()
            for u in adj[v]:
                if not vis[u]:
                    size += 1
                    vis[u] = True
                    q.append(u)
        return size
    b = 0
    for i in range(n):
        b = max(dfs(i), b)
    print(b)
                    


t = ni()
adj = [[] for _ in range(t)]
cords = []
for case in range(t):
    x, y, d = nl()
    cords.append((x,y,d))
    
for i in range(t):
    for j in range(t):
        if i != j:
            d = math.sqrt((cords[i][0] - cords[j][0])**2 + ((cords[i][1] - cords[j][1])**2))
            if d <= cords[i][2]: adj[i].append(j)
            if d <= cords[j][2]: adj[j].append(i)
        
    
solve(t, adj)
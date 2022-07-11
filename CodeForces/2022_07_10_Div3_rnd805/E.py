import sys
from collections import *
sys.setrecursionlimit(10**5)
itr = (line for line in sys.stdin.read().strip().split('\n'))
INP = lambda: next(itr)
def ni(): return int(INP())
def nl(): return [int(_) for _ in INP().split()]



def solve():
    n = ni()
    cnt = [0 for _ in range(n+1)]
    g = [[] for _ in range(n+1)]
    doms = []
    pos = True
    for _ in range(n):
        a,b = nl()
        if a == b:
            pos = False
        cnt[a] += 1
        cnt[b] += 1
        g[a].append(b)
        g[b].append(a)
        
        doms.append((a,b))
    for c in cnt:
        if c > 2:
            return "NO"
    if not pos:
        return "NO"
    #print(g)
    
    def dfs(s, vis):
        stack = [s]
        count = 0
        vis[s] = True
        while stack:
            #print(vis)
            node = stack.pop()
            count += 1
            for v in g[node]:
                if vis[v] == -1:
                    stack.append(v)
                    vis[v] = True
        return count, vis
    
    
    comp = 0
    vis = [-1 for _ in range(n+1)]
    for i in range(1, n+1):
        if vis[i] == -1:
            #print(i)
            comp, vis = dfs(i, vis)
            #print(comp)
            if comp % 2 == 1:
                return "NO"
    
    
    return "YES"


t = ni()
for case in range(t):
    print(solve())

    
        
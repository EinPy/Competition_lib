import sys
from collections import *
sys.setrecursionlimit(10**5)
itr = (line for line in sys.stdin.read().strip().split('\n'))
INP = lambda: next(itr)
def ni(): return int(INP())
def nl(): return [int(_) for _ in INP().split()]



def solve(n,m,g):
    #print(g)
    vis = [[0] * m for _ in range(n)]
    #print(vis)
    def dfs(r, c):
        q = [(r,c)]
        vis[r][c] = 1
        g[r][c] = 'W'
        while q:
            cr, cc = q.pop()
            for rn, cn in [(r+1,c), (r-1,c), (r, c+1), (r, c-1)]:
                if rn >= 0 and rn < n and cn >= 0 and cn <m:
                    print(rn, cn, n, m, len(vis), len(vis[0]))
                    if vis[rn][cn] == 0: 
                        if g[rn][cn] != '-':
                            if g[cr][cc] == 'W':
                                g[rn][cn] = 'B'
                                vis[rn][cn] = 1
                                q.append((rn,cn))
                            else: 
                                g[rn][cn] = 'W'
                                vis[rn][cn] = 1
                                q.append((rn,cn))
                            
                            print("ghap")
    calls = 0
    for r in range(n):
        for c in range(m):
            if vis[r][c] == 0 and g[r][c] != '-':
                dfs(r,c)
                calls += 1
        
    for e in g:
        print(''.join(e))
    print(g[2][27], g[2][28], calls)

n ,m = nl()
g = []
for _ in range(n):
    a = list(INP())
    g.append(a)
    
solve(n,m,g)
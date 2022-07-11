import sys
from collections import *
sys.setrecursionlimit(10**5)
itr = (line for line in sys.stdin.read().strip().split('\n'))
INP = lambda: next(itr)
def ni(): return int(INP())
def nl(): return [int(_) for _ in INP().split()]



def solve(row, col ,g):
    cnt = {'.' : 0, "B":0,"G":0,'#':0}
    bad = []
    for r in range(row):
        for c in range(col):
            cnt[g[r][c]] += 1
            if g[r][c] == "B":
                for nr, nc in [(r-1,c), (r+1, c), (r, c+1), (r,c-1)]:
                    if 0 <= nr < row and 0 <= nc < col:
                        if g[nr][nc] == '.':
                            g[nr][nc] = '#'
            
    vis = [[False for _ in range(col)] for _ in range(row)]

    def bfsGrid(r, c):
        rG = 0
        rB = 0
        q = deque([(r,c)])
        vis[r][c] = True
        clear = True
        
        while q:
            r, c= q.popleft()
            for nr, nc in [(r-1,c), (r+1, c), (r, c+1), (r,c-1)]:
                if 0 <= nr < row and 0 <= nc < col:
                    tup = nr, nc
                    if not vis[nr][nc] and g[nr][nc] != '#':
                            vis[nr][nc] = True
                            q.append(tup)
                            if g[nr][nc] == "G":
                                rG +=1
                            if g[nr][nc] == "B": clear = False
                            
        return rG, rB, clear
    
    rG, rB, ans = bfsGrid(row-1, col-1)
    if cnt["G"] == 0:
        print("YES")
    elif not ans:
        print("NO")
    elif rG == cnt["G"]:
        print("YES")
    else:
        print("NO")


t = ni()
for case in range(t):
    n, m = nl()
    g = []
    for _ in range(n):
        g.append(list(INP()))
    solve(n,m,g)
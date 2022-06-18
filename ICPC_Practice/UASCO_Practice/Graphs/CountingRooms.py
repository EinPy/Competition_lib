#solution to http://www.usaco.org/index.php?page=viewproblem2&cpid=992
import sys
from collections import *
sys.setrecursionlimit(10**5)
itr = (line for line in sys.stdin.read().strip().split('\n'))
INP = lambda: next(itr)
def ni(): return int(INP())
def nl(): return [int(_) for _ in INP().split()]



def solve(n,a):
    pass


R, C = nl()
g = []
for _ in range(R): g.append(list(INP()))

vis = [[False for _ in range(C)] for _ in range(R)]
#bfs when graph is grid
#can return visited if you want to find how many connected graphs there are
def bfsGrid(r, c):
    q = deque([(r,c)])
    vis[r][c] = True
    while q:
        r, c= q.popleft()
        for nr, nc in [(r-1,c), (r+1, c), (r, c+1), (r,c-1)]:
            if 0 <= nr < R and 0 <= nc < C:
                tup = nr, nc
                if not vis[nr][nc]:
                    if g[nr][nc] == '.': #add other conditions here
                        vis[nr][nc] = True
                        q.append(tup)
    return vis

room = 0
for i in range(R):
    for j in range(C):
        if not vis[i][j]:
            if g[i][j] == '.':
                bfsGrid(i, j)
                room += 1
print(room)
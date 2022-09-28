import sys
from collections import *
sys.setrecursionlimit(10**5)
itr = (line for line in sys.stdin.read().strip().split('\n'))
INP = lambda: next(itr)
def ni(): return int(INP())
def nl(): return [int(_) for _ in INP().split()]



#bfs when graph is grid
#can return visited if you want to find how many connected graphs there are
def bfsGrid(grid, r, c):
    R = len(grid)
    C = len(grid[0])
    q = deque([(r,c)])
    dists = [[-1 for _ in range(C)] for _ in range(R)]
    dists[r][c] = 0
    while q:
        r,c = q.popleft()
        diff = grid[r][c]
        for nr, nc in [(r-diff,c), (r+diff, c), (r, c+diff), (r,c-diff)]:
            if 0 <= nr < R and 0 <= nc < C:
                tup = nr, nc
                if dists[nr][nc] == -1: #add other conditions here
                    if nr == R-1 and nc == C-1:
                        return dists[r][c] + 1
                    dists[nr][nc] = dists[r][c] + 1
                    q.append(tup)
    return -1

row, col = nl()
g = [[] for _ in range(row * col)]
gra = []
for r in range(row):
    num = list(map(int,list(INP())))
    gra.append(num)
#for l in gra:
#    print(l)
print(bfsGrid(gra, 0, 0,))
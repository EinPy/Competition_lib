import sys
from collections import *
sys.setrecursionlimit(10**5)
itr = (line for line in sys.stdin.read().strip().split('\n'))
INP = lambda: next(itr)
def ni(): return int(INP())
def nl(): return [int(_) for _ in INP().split()]


#bfs when graph is grid
#can return visited if you want to find how many connected graphs there are
def bfsGrid(grid, start):
    R = len(grid)
    C = len(grid[0])
    q = deque(start)
    dists = [[-1 for _ in range(C)] for _ in range(R)]
    for r, c in start:
        dists[r][c] = 0
    while q:
        r,c = q.popleft()
        for nr, nc in [(r-1,c), (r+1, c), (r, c+1), (r,c-1)]:
            if 0 <= nr < R and 0 <= nc < C:
                tup = nr, nc
                if dists[nr][nc] == -1 and grid[nr][nc] != "#" and grid[nr][nc] != "J": #add other conditions here
                    dists[nr][nc] = dists[r][c] + 1
                    q.append(tup)
    return dists

#bfs when graph is grid
#can return visited if you want to find how many connected graphs there are
def bfsGrid2(grid,grid2, r, c):
    R = len(grid)
    C = len(grid[0])
    q = deque([(r,c)])
    dists = [[-1 for _ in range(C)] for _ in range(R)]
    dists[r][c] = 0
    while q:
        r,c = q.popleft()
        for nr, nc in [(r-1,c), (r+1, c), (r, c+1), (r,c-1)]:
            if 0 <= nr < R and 0 <= nc < C:
                tup = nr, nc
                if dists[nr][nc] == -1 and (grid[nr][nc] == "." or grid[nr][nc] == "J") and grid[nr][nc] != "F": #add other conditions here
                    dists[nr][nc] = dists[r][c] + 1
                    q.append(tup)
    return dists

rows, col = nl()
m = []
f = []
start = (0,0)
for r in range(rows):
    row = list(INP())
#    print(r)
    for c in range(col):
        if row[c] == "J":
            start = (r, c)
        if row[c] == "F":
            f.append((r, c))
    m.append(row)
    
dists = bfsGrid(m, f)
#for l in dists: print(l)
ex = bfsGrid2(m,dists, start[0], start[1])
#print()
#for l in ex: print(l)

best = 1e9
found = False
for i in range(rows):
    for j in range(col):
        if i == 0 or i == rows -1 or  j == 0 or j == col -1:
            if  ex[i][j] < dists[i][j] and ex[i][j] != -1 and m[i][j] == ".":
                found = True
                best = min(best,ex[i][j] + 1)
            if m[i][j] == "J":
                best = 1
                found = True
            if ex[i][j] != -1 and dists[i][j] == -1:
                best = min(ex[i][j]+1,best)
                found = True
if found:   
    print(best)
else:
    print("IMPOSSIBLE")
    
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
        for nr, nc in [(r-1,c), (r+1, c), (r, c+1), (r,c-1)]:
            if 0 <= nr < R and 0 <= nc < C:
                tup = nr, nc
                if dists[nr][nc] == -1 and grid[nr][nc] != "#": #add other conditions here
                    dists[nr][nc] = dists[r][c] + 1
                    q.append(tup)
    return dists


tr = {"N": (-1, 0), "S": (1, 0), "W" : (0, -1), "E": (0, 1)}
#bfs when graph is grid
#can return visited if you want to find how many connected graphs there are
def bfsGrid2(grid, r, c, inst):
    R = len(grid)
    C = len(grid[0])
    q = deque([(r,c)])
    dists = [[-1 for _ in range(C)] for _ in range(R)]
    dists[r][c] = 0
    while q:
        r,c = q.popleft()
        if dists[r][c] == len(inst):
            break
        for nr, nc in [(r-1,c), (r+1, c), (r, c+1), (r,c-1)]:
            if (nr -r,nc - c) != tr[inst[dists[r][c]]]:
#                print(nr,nc, "here")
                if 0 <= nr < R and 0 <= nc < C:
                    tup = nr, nc
                    if dists[nr][nc] == -1 and grid[nr][nc] != "#": #add other conditions here
                        dists[nr][nc] = dists[r][c] + 1
                        q.append(tup)
    return dists



w, h = nl()
m = []
start = (0,0)
for r in range(h):
    row = list(INP())
#    print(r)
    for c in range(w):
        if row[c] == "S":
            start = (r, c)
    m.append(row)
    
d = list(INP())
#print(start)
check = bfsGrid(m,start[0],start[1])
arr = bfsGrid2(m,start[0],start[1], d)
#for l in check:
#    print(l)
#print()
#for l in arr:
#    print(l)

for i in range(h):
    for j in range(w):
        if check[i][j] == arr[i][j] and check[i][j] != -1 and m[i][j] != "S" and check[i][j] == len(d):
            m[i][j] = "!"
            
for l in m:
    print(''.join(l))


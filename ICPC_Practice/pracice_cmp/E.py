import sys
from collections import *
sys.setrecursionlimit(10**5)
itr = (line for line in sys.stdin.read().strip().split('\n'))
INP = lambda: next(itr)
def ni(): return int(INP())
def nl(): return [int(_) for _ in INP().split()]



def solve(n,a):
    pass


#for each pass, store minimum elevation for each heigth

R, C, N = nl()
G= []
for r in range(R):
    a = nl()
    G.append(a)
    
def isPass(r,c):
    #not on edege
    if r > 0 and r < R -1 and c > 0 and c < C -1:
        #not adjecent to undrivable
        if G[r+1][c] != -1 and G[r-1][c] != -1 and G[r][c+1] != -1 and G[r][c-1] != -1:
            if G[r][c+1] < G[r][c] and G[r][c-1] < G[r][c]:
                if G[r+1][c] > G[r][c] and G[r-1][c] > G[r][c]:
                    return True
    return False

#bfs when graph is grid
#can return visited if you want to find how many connected graphs there are
def bfsGrid():
    start = []
    for r in range(R):
        if G[r][0] != -1:
            #curRow, curCol, number of passes
            start.append((r,0,0))
    q = deque(start)
    #structure [row][col][distsance for each amount of passes]
    dists = [[[-1] * (N+1) for _ in range(C)] for _ in range(R)]
    #print([-1] * (N+1))
    #print(start)
    for (r, c, p) in start:
        dists[r][c][0] = G[r][c]
    print(dists)
    #print(start)
    # for r in range(R):
    #     print(dists[r][C-1])
    while q:
        r,c, passes = q.popleft()
        if passes <= N:
            #3 directions
            for nr, nc in [(r, c+1), (r+1, c+1), (r-1,c+1)]:
                #cannot go to a block
                if 0 <= nr < R and 0 <= nc < C and G[nr][nc] != -1:
                    if isPass(nr,nc) and passes + 1 <= N:
                        if dists[nr][nc][passes + 1] == -1:
                            dists[nr][nc][passes+1] = dists[r][c][passes] + G[nr][nc]
                            q.append((nr,nc,passes+1))
                        elif dists[nr][nc][passes+1] > dists[r][c][passes] + G[nr][nc]:
                            dists[nr][nc][passes+1] = dists[r][c][passes] + G[nr][nc]
                            q.append((nr,nc,passes+1))
                    else:
                        if dists[nr][nc][passes] == -1:
                            dists[nr][nc][passes] = dists[r][c][passes] + G[nr][nc]
                            q.append((nr, nc, passes))
                        elif dists[nr][nc][passes] > dists[r][c][passes] + G[nr][nc]:
                            dists[nr][nc][passes] = dists[r][c][passes] + G[nr][nc]
                            q.append((nr,nc,passes))
    # for r in range(R):
    #     print(r, dists[r][1])
    # for r in range(R):
    #     print(dists[r][C-1])
    best = 100000000000
    for r in range(R):
        if dists[r][C-1][N] != -1:
            best = min(best,dists[r][C-1][N])
    if best == 100000000000:
        print("impossible")
    else:
        print(best)
        
bfsGrid()
import sys
from collections import *
sys.setrecursionlimit(10**5)
itr = (line for line in sys.stdin.read().strip().split('\n'))
INP = lambda: next(itr)
def ni(): return int(INP())
def nl(): return [int(_) for _ in INP().split()]


#bfs when graph is grid
#can return visited if you want to find how many connected graphs there are
def bfsGrid(grid, r, c, rf, cf):
    # if r == rf and c == cf:
    #     return []
    R = len(grid)
    C = len(grid[0])
    q = deque([(r,c)])
    dists = [[-1 for _ in range(C)] for _ in range(R)]
    parent = [[-1 for _ in range(C)] for _ in range(R)]
    dists[r][c] = 0
    while q:
        r,c = q.popleft()
        for nr, nc in [(r-1,c), (r+1, c), (r, c+1), (r,c-1)]:
            if 0 <= nr < R and 0 <= nc < C:
                tup = nr, nc
                if (dists[nr][nc] == -1 or dists[nr][nc] > dists[r][c]+1) and grid[nr][nc] != False: #add other conditions here
                    dists[nr][nc] = dists[r][c] + 1
                    parent[nr][nc] = (r, c)
                    q.append(tup)
    if dists[rf][cf] == -1:
        return False
    else:
        path = []
        curr = rf, cf
        while curr != -1:
            path.append(curr)
            curr = parent[curr[0]][curr[1]]
    return path


row, col = nl()
G = [[True for _ in range(col+1)] for _ in range(row+1)]
a1r, a1c = nl()
a2r, a2c = nl()
b1r, b1c = nl()
b2r, b2c = nl()

bestL = 10**18

#set shortest path both orders, save dirction

#test A short, B long
G[b1r][b1c] = False
G[b2r][b2c] = False #no shared verticies
pos = False
patha = bfsGrid(G, a1r, a1c, a2r, a2c)

for a, b in patha:
    G[a][b] = False    
        
G[b1r][b1c] = True
G[b2r][b2c] = True #no shared verticies

pathb = bfsGrid(G, b1r, b1c, b2r, b2c)
if pathb != False:
    pos = True
    bestL = len(patha)-1 + len(pathb)-1

#now test other way, b first then a
G = [[True for _ in range(col+1)] for _ in range(row+1)]
G[a1r][a1c] = False
G[a2r][a2c] = False #no shared verticies

pathb = bfsGrid(G, b1r, b1c, b2r, b2c)    

for a, b in pathb:
    G[a][b] = False

G[a1r][a1c] = True
G[a2r][a2c] = True #no shared verticies

patha = bfsGrid(G, a1r, a1c, a2r, a2c)
if patha != False:

    pos = True
    bestL = min(bestL, len(patha)-1+ len(pathb)-1)


if pos:
    print(bestL)
else:
    print("IMPOSSIBLE")    
    
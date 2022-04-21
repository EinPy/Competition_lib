import sys
from collections import *
sys.setrecursionlimit(10**5)
itr = (line for line in sys.stdin.read().strip().split('\n'))
INP = lambda: next(itr)
def ni(): return int(INP())
def nl(): return [int(_) for _ in INP().split()]





def solve(grid,row,col):
    newG = [['.' for _ in range(col)] for _ in range(row)]
    for c in range(col):
        stones = []
        free = 0
        for r in range(row-1,-1,-1):
#            print(r,c)
            if grid[r][c] == '*':
                if not stones:
                    free += 1
                else:
                    stones[-1][1] += 1
            elif grid[r][c] == "o":
                newG[r][c] = "o"
                stones.append([r,0])
                
        for f in range(free):
            newG[row-1-f][c] = "*"
        if stones:
            for s in stones:
                i, ree = s
                for p in range(ree):
                    newG[i-1 - p][c] = "*"
            
    for line in newG:
        print(''.join(line))
    print()
            
            
            


t = ni()
for c in range(t):
    n, m = nl()
    grid = []
    for r in range(n):
        grid.append(INP())
#    print(grid)
    solve(grid,n,m)
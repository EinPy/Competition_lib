import sys
from collections import *
sys.setrecursionlimit(10**5)
itr = (line for line in sys.stdin.read().strip().split('\n'))
INP = lambda: next(itr)
def ni(): return int(INP())
def nl(): return [int(_) for _ in INP().split()]




def solve(row, col, grid):
    top, left, fewTotStep = 10, 10, 100 
    steps = []
    for r in range(row):
        for c in range(col):
            if grid[r][c] == 'R':
                top = min(top, r)
                left = min(left, c)
                steps.append((r,c))

    for el in steps:
        if el[0] <= top and el[1] <= left:
            return "YES"

    return "NO"

t = ni()
for _ in range(t):
    r, c = nl()
    grid = []
    for row in range(r):
        grid.append(list(INP()))
    #print(grid)
    print(solve(r, c, grid))
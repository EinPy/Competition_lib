import sys
from collections import *
sys.setrecursionlimit(10**5)
itr = (line for line in sys.stdin.read().strip().split('\n'))
INP = lambda: next(itr)
def ni(): return int(INP())
def nl(): return [int(_) for _ in INP().split()]



def solve(n,a):
    pass


t = ni()
for case in range(t):
    a, b = nl()
    grid = [[0 for _ in range(a)] for _ in range(b)]
    n, m = nl()
    
    card = ["N", "E", "S", "W"]
    #direction, x, y
    robots = [[0, 0, 0] for _ in range(n)]
    for i in range(n):
        X, Y, C = list(INP().split())
        #to 0-index
        X = int(X)
        Y = int(Y)
        X -= 1
        Y -= 1
        X, Y = Y, X
        robots[i][0] = X
        robots[i][1] = Y
        robots[i][2] = card.index(C)
        grid[X][Y] = "*"
    for l in grid:print(l)
    print(robots)
    
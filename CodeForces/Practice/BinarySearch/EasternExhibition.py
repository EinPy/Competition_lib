import sys
from collections import *
sys.setrecursionlimit(10**5)
itr = (line for line in sys.stdin.read().strip().split('\n'))
INP = lambda: next(itr)
def ni(): return int(INP())
def nl(): return [int(_) for _ in INP().split()]



def solve(n,x,y):
    x.sort()
    y.sort()
    xDiff = x[n//2] - x[(n-1) // 2] + 1 
    yDiff = y[n//2] - y[(n-1) // 2] + 1
    print(xDiff * yDiff)
    
#. - - . - - .
#[0, 3, 6]
#left: 1, right: 1

t = ni()
for case in range(t):
    n = ni()
    x, y = [], []
    for _ in range(n):
        nx, ny = nl()
        x.append(nx)
        y.append(ny)
    solve(n,x, y)
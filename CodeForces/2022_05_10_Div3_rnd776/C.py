import sys
from collections import *
sys.setrecursionlimit(10**5)
itr = (line for line in sys.stdin.read().strip().split('\n'))
INP = lambda: next(itr)
def ni(): return int(INP())
def nl(): return [int(_) for _ in INP().split()]





def solve(n, m, points):
    #print(points)
    points.sort()
    use = []
    #print(points)
    tot = 0
    for i in range(n*2):
        tot += points[i][0]
        use.append((points[i][1], points[i][2]))
    
    print(tot)
    use.sort()
    l, r = 0, len(use)-1
    while l < r:
        print(f"{use[l][1]+1} {use[r][1]+1}")
        l += 1
        r -= 1
    
    print()
    



t = ni()
for case in range(t):
    empty = INP()
    n, m = nl()
    points = []
    for p in range(m):
        x, w = nl()
        points.append((w,x,p))
    solve(n, m, points)
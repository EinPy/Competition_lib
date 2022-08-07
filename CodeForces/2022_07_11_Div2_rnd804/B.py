import sys
from collections import *
sys.setrecursionlimit(10**5)
itr = (line for line in sys.stdin.read().strip().split('\n'))
INP = lambda: next(itr)
def ni(): return int(INP())
def nl(): return [int(_) for _ in INP().split()]



def solve(n,m):
    g = [[0 for _ in range(m)] for _ in range(n)]
    #strat with inverting squares
    g[0][0] = 1
    one = False
    cnt = 0
    cntR = 0
    row0 = True
    for r in range(n):
        if r == 0:
            for c in range(1,m):
                if one:
                    g[r][c] = 1
                    cnt += 1
                    if cnt == 2: 
                        one = False
                        cnt = 0
                else:
                    g[r][c] = 0
                    cnt += 1
                    if cnt == 2:
                        one = True
                        cnt = 0
        else:
            cnt = 0
            if row0:
                g[r][0] = 0
                cntR += 1
                if cntR == 2:
                    row0 = False
                    cntR = 0
                one = True
            else:
                g[r][0] = 1
                cntR += 1
                if cntR == 2:
                    row0 = True
                    cntR = 0
                one = False
            for c in range(1,m):
                if one:
                    g[r][c] = 1
                    cnt += 1
                    if cnt == 2: 
                        one = False
                        cnt = 0
                else:
                    g[r][c] = 0
                    cnt += 1
                    if cnt == 2:
                        one = True
                        cnt = 0
                

    for r in g:
        print(' '.join(map(str,r)))
t = ni()
for case in range(t):
    n,m = nl()
    solve(n,m)
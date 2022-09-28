import sys
from collections import *
sys.setrecursionlimit(10**5)
itr = (line for line in sys.stdin.read().strip().split('\n'))
INP = lambda: next(itr)
def ni(): return int(INP())
def nl(): return [int(_) for _ in INP().split()]



n, m, cnt = nl()
c = 0
out = []
for r in range(n):
    for j in range(m):
        out.append((r+1, j+1))
        if r % 2 == 0:
            for c in range(m):
                
        else:
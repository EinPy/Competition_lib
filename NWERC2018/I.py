import sys
from collections import *
sys.setrecursionlimit(10**5)
itr = (line for line in sys.stdin.read().strip().split('\n'))
INP = lambda: next(itr)
def ni(): return int(INP())
def nl(): return [int(_) for _ in INP().split()]



n = ni()
gas = [i for i in range(1,n+1)]
h = nl()
h.sort()
best = 1
pos = True
for i in range(n):
    if h[i] <= gas[i]:
        best = min(best, h[i] /(gas[i]))
    else:
        pos = False
if not pos:
    print("impossible")
else:
    print(best)
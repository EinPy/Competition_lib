import sys
from collections import *
sys.setrecursionlimit(10**5)
itr = (line for line in sys.stdin.read().strip().split('\n'))
INP = lambda: next(itr)
def ni(): return int(INP())
def nl(): return [int(_) for _ in INP().split()]



t, s, n = nl()
l = s
u = 0
lIsDown = True
flips = nl()

cT = 0
for f in flips:
    d = f - cT
    cT += d
    if lIsDown:
        p = min(d, u)
        u -= p
        l += p
    else:
        p = min(d, l)
        l -= p
        u += p
    if lIsDown:
        lIsDown = False
    else:
        lIsDown = True
    
d = t - cT
if lIsDown:
    print(max(u - d, 0))
else:
    print(max(l - d, 0))
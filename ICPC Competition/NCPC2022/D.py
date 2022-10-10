import sys
from collections import *
sys.setrecursionlimit(10**5)
itr = (line for line in sys.stdin.read().strip().split('\n'))
INP = lambda: next(itr)
def ni(): return int(INP())
def nl(): return [int(_) for _ in INP().split()]


import math
r = ni()
best = 1e9
bx, by = 0, 0
for i in range(r+1):
    h = math.ceil(math.sqrt(r*r - i*i))
    rad = math.sqrt(h*h + i*i)
    if rad <= r:
        h += 1
    rad = math.sqrt(h*h + i*i)
    if rad < best:
        best = rad
        bx = i
        by = h
        
print(bx, by)

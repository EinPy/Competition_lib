import sys
from collections import *
sys.setrecursionlimit(10**5)
itr = (line for line in sys.stdin.read().strip().split('\n'))
INP = lambda: next(itr)
def ni(): return int(INP())
def nl(): return [int(_) for _ in INP().split()]

import math


# Distance between two points
def dist(p, q):
    return math.hypot(p[0]-q[0], p[1] - q[1])

def solve(s1, s2, f1, f2):
    #shortest distance at any piont cannot chekc all points. 
    #convert pts to line
    print(max(dist(s1, s2), dist(f1, f2)))
    pass


s1x, s1y, s2x, s2y, f1x, f1y, f2x, f2y = nl()
s1 = (s1x, s1y)
s2 = (s2x, s2y)
f1 = (f1x, f1y)
f2 = (f2x, f2y)

solve(s1, s2, f1, f2)
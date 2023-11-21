import sys
from collections import *
sys.setrecursionlimit(10**5)
itr = (line for line in sys.stdin.read().strip().split('\n'))
INP = lambda: next(itr)
def ni(): return int(INP())
def nl(): return [int(_) for _ in INP().split()]

import math
import random
# Distance between two points
def dist(p, q):
    return math.hypot(p[0]-q[0], p[1] - q[1])
    #sample points

def solve(ufo):
    #sample random pionts
    pts = []
    maxX, maxY = 0, 0
    for i in range(1000000):
        pts.append((random.uniform(-10, 20),random.uniform(-10, 20)))
    inside = 0
    for p in pts:
        for u in ufo:
            if dist((u[0], u[1]), p) <= u[2]:
                inside += 1
                break
    #print(maxX, maxY)
    #print(pts[:10])
    print((inside/1000000)* 30 * 30)
    

t = ni()
ufo = []
for case in range(t):
    ufo.append(nl())
    
solve(ufo)
    
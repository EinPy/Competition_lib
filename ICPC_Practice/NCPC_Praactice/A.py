import sys
from collections import *
sys.setrecursionlimit(10**5)
itr = (line for line in sys.stdin.read().strip().split('\n'))
INP = lambda: next(itr)
def ni(): return int(INP())
def nl(): return [int(_) for _ in INP().split()]


import math

t = ni()
cubes = []
cyls = []
for _ in range(t):
    a, b = INP().split()
    if a == "cube":
        cubes.append(b)
    else:
        cyls.append(b)
    
out = [("dummy", 1e5)]
cubes.sort(reverse=True)
cyls.sort(reverse=True)


def run():
    while len(cubes) != 0 and len(cyls) != 0:
        if cubes and cyls:
            d = max(2* cyls[-1], math.sqrt(2) * cubes[-1])
            t = -1
            prev = out[-1][0]
            if prev == "cube":
                t = 1
            if prev == "cylinder":
                t = 0
            sel = 1
            if d == 2 * cyls[-1]:
                sel = 0
            if prev == 1:
                
            
            if out[-1][-1] > d:
                return False
            if d == cyls[-1] *2:
                out.append(("cylinder", cyls[-1]))
                cyls.pop()
            else:
                out.append(("cube", cubes[-1]))
                cubes.pop()
    while len(cubes) != 0:
        d = cubes[-1] * math.sqrt(2)
        if out[-1][-1] > d:
                return False
        out.append(("cube", cubes[-1]))
        cubes.pop()
        
    while len(cyls) != 0:
        d = cyls[-1] * 2
        if out[-1][-1] > d:
                return False
        out.append(("cube", cubes[-1]))
        cubes.pop()
                
                
        
    
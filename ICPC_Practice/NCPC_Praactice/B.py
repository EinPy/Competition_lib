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
tot = []
for _ in range(t):
    a, b = INP().split()
    b = int(b)
    if a == "cube":
        cubes.append(b)
        tot.append((b, "cube", b))
    else:
        tot.append((b * 2, "cylinder", b))
        
tot.sort()
print(tot)
def run():
    for i in range(len(tot)-1):
        if tot[i][0] == tot[i][2]:
            
for el in tot:
    print(el[1], el[2])
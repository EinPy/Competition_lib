import sys
from collections import *
sys.setrecursionlimit(10**5)
itr = (line for line in sys.stdin.read().strip().split('\n'))
INP = lambda: next(itr)
def ni(): return int(INP())
def nl(): return [int(_) for _ in INP().split()]



N, T, G = nl()

p = []
for l in range(N):
    a = ni()
    a = a% (2*T)
    p.append(a)
p.sort()
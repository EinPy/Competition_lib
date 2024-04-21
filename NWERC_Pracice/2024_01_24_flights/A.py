import sys
from collections import *
sys.setrecursionlimit(10**5)
itr = (line for line in sys.stdin.read().strip().split('\n'))
INP = lambda: next(itr)
def ni(): return int(INP())
def nl(): return [int(_) for _ in INP().split()]


k, n, m = nl()
curr = [0] * k
for _ in range(m):
    u, v, d, z = nl()
    
for _ in range(k * n):
    a, b, c = nl()
    
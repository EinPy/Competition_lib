import sys
from collections import *
sys.setrecursionlimit(10**5)
itr = (line for line in sys.stdin.read().strip().split('\n'))
INP = lambda: next(itr)
def ni(): return int(INP())
def nl(): return [int(_) for _ in INP().split()]





def solve(arr):
    pass



n, m, q = nl()
g = []
for row in range(n):
    r = INP()
    g.append(r.split())
print(g)
for case in range(q):
    r, c = nl()
    arr = nl()

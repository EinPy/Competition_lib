import sys
from collections import *
sys.setrecursionlimit(10**5)
itr = (line for line in sys.stdin.read().strip().split('\n'))
INP = lambda: next(itr)
def ni(): return int(INP())
def nl(): return [int(_) for _ in INP().split()]



def solve(n,a):
    out = [0 for _ in range(n)]
    used = [0 for _ in range(n)]
    for i in range(n):
        if a[i] == i+1:
            out[i] = 1
        



t = ni()
for case in range(t):
    n = ni()
    a = nl()
    solve(n,a)
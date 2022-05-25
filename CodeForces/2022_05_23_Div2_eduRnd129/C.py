import sys
from collections import *
sys.setrecursionlimit(10**5)
itr = (line for line in sys.stdin.read().strip().split('\n'))
INP = lambda: next(itr)
def ni(): return int(INP())
def nl(): return [int(_) for _ in INP().split()]



def solve(n, a, b):
    pass


t = ni()
for case in range(t):
    n = ni()
    a = nl()
    b = nl()
    solve(n, a, b)
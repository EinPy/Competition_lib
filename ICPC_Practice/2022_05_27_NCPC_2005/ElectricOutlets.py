import sys
from collections import *
sys.setrecursionlimit(10**5)
itr = (line for line in sys.stdin.read().strip().split('\n'))
INP = lambda: next(itr)
def ni(): return int(INP())
def nl(): return [int(_) for _ in INP().split()]



def solve(a):
    p = 0
    n = len(a)
    for i in range(1, n):
        p += a[i] - 1
    p += 1
    print(p)
        


t = ni()
for case in range(t):
    a = nl()
    solve(a)
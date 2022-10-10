import sys
from collections import *
sys.setrecursionlimit(10**5)
itr = (line for line in sys.stdin.read().strip().split('\n'))
INP = lambda: next(itr)
def ni(): return int(INP())
def nl(): return [int(_) for _ in INP().split()]



def solve(n,a, b):
    if a == b:
        print(0)
        return
    za = a.count(0)
    zb = b.count(0)
    diff = 0
    for i in range(n):
        if a[i] != b[i]:
            diff += 1
    ops = min(1  + abs(a.count(0) - b.count(0)), diff)
    print(ops)
    


t = ni()
for case in range(t):
    n = ni()
    b = nl()
    a = nl()
    solve(n,a, b)
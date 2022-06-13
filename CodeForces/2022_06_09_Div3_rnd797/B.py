import sys
from collections import *
sys.setrecursionlimit(10**5)
itr = (line for line in sys.stdin.read().strip().split('\n'))
INP = lambda: next(itr)
def ni(): return int(INP())
def nl(): return [int(_) for _ in INP().split()]



def solve(n,a, b):
    pos = True
    diff = a[0] - b[0]
    for i in range(n):
        if a[i] < b[i]:
            pos = False
        if a[i] - b[i] != diff:
            if b[i] != 0:
                pos = False
    if pos: print("YES")
    else: print("NO")

t = ni()
for case in range(t):
    n = ni()
    a = nl()
    b = nl()
    solve(n,a, b)
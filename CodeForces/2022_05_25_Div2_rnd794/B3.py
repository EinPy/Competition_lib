import sys
from collections import *
sys.setrecursionlimit(10**5)
itr = (line for line in sys.stdin.read().strip().split('\n'))
INP = lambda: next(itr)
def ni(): return int(INP())
def nl(): return [int(_) for _ in INP().split()]



def solve(n,a):
    i = 0
    inv = 0
    while i <= n-2:
        if a[i] > a[i+1]:
            inv += 1
            i += 1
        i += 1
    print(inv)


t = ni()
for case in range(t):
    n = ni()
    a = nl()
    solve(n,a)
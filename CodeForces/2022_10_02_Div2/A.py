import sys
from collections import *
sys.setrecursionlimit(10**5)
itr = (line for line in sys.stdin.read().strip().split('\n'))
INP = lambda: next(itr)
def ni(): return int(INP())
def nl(): return [int(_) for _ in INP().split()]



def solve(n):
    if n - 3 <= 3:
        print(0)
    else:
        print((n - 3) // 3 - 1)


t = ni()
for case in range(t):
    n = ni()
    solve(n)
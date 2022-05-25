import sys
from collections import *
sys.setrecursionlimit(10**5)
itr = (line for line in sys.stdin.read().strip().split('\n'))
INP = lambda: next(itr)
def ni(): return int(INP())
def nl(): return [int(_) for _ in INP().split()]


import math

def solve(n):
    #solved problem equation to a**2 = 2b + 1
    #this only has integer solution for odd a
    ans = 0
    for a in range(3, 10**5,2):
        b = (a**2 - 1) / 2
        if math.sqrt(a**2 + b ** 2) <= n:
            ans += 1
        else:
            break
    print(ans)


t = ni()
for case in range(t):
    n = ni()
    solve(n)
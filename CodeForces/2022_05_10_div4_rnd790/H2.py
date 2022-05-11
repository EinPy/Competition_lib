#To start code
import sys
from collections import *
sys.setrecursionlimit(10**5)
itr = (line for line in sys.stdin.read().strip().split('\n'))
INP = lambda: next(itr)
def ni(): return int(INP())
def nl(): return [int(_) for _ in INP().split()]


#code




def solve(n,a):
    c =0
    points = [0 for _ in range(n)]

    for i in range(n-1):
        if a[i] < i:
            points[i] += 1

    for i in range(n-1):
        for j in range(i,a[i]):
            c += points[j]

    print(points)
    return c



t = ni()
for case in range(t):
    n = ni()
    a = nl()
    print(solve(n,a))
import sys
from collections import *
sys.setrecursionlimit(10**5)
itr = (line for line in sys.stdin.read().strip().split('\n'))
INP = lambda: next(itr)
def ni(): return int(INP())
def nl(): return [int(_) for _ in INP().split()]



def solve(n,a):
    a.sort()
    a = [1e6] + a + [1e6]
    d1, d2 = 1e6, 1e6
    i1, i2 = -1, -1 
    for i in range(1, n+1):
        diff = min(abs(a[i+1]-a[i]), abs(a[i-1]-a[i]))
        if diff <= d1:
            d2 = d1
            d1 = diff
            i2 = i1
            i1 = i
    a.pop(max(i1,i2))
    a.pop(min(i1,i2))
    a.pop(0)
    a.pop(-1)
    inst = 0
    for i in range(0,n, 2):
        inst += abs(a[i+1] - a[i])
    print(inst)

    



n = ni()
a = nl()
solve(n,a)
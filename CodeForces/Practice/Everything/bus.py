import sys
from collections import *
sys.setrecursionlimit(10**5)
itr = (line for line in sys.stdin.read().strip().split('\n'))
INP = lambda: next(itr)
def ni(): return int(INP())
def nl(): return [int(_) for _ in INP().split()]



def solve(n):
    if n % 2 != 0 or n == 2:
        print(-1)
        return
    mi, ma = 1e20, -1
    if n % 4 == 0 or n % 4 == 2:
        ma  = n // 4
    if n % 6 == 0:
        mi = n // 6
    if n % 6 == 2:
        mi = (n - 8) // 6 + 2
    if n % 6 == 4:
        mi = n // 6 + 1
    
    
    if ma == -1 and mi != 1e20:
        ma = mi
    if mi == 1e20 and ma != -1:
        mi = ma
    

    if mi == 1e20 and ma == -1:
        print(-1)
    else:
        print(mi, ma)



t = ni()
for case in range(t):
    n = ni()
    (solve(n))
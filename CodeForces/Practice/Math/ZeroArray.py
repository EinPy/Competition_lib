from distutils.errors import CompileError

import sys
from collections import *
sys.setrecursionlimit(10**5)
itr = (line for line in sys.stdin.read().strip().split('\n'))
INP = lambda: next(itr)
def ni(): return int(INP())
def nl(): return [int(_) for _ in INP().split()]



def solve(n,a):
    ma = 0
    for i in range(n):
        ma = max(ma, a[i])

    if sum(a) - ma >= ma and sum(a) % 2 == 0:
        print("YES")
    else: print("NO")


n = ni()
a = nl()
solve(n,a)
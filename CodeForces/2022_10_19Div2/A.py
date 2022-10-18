import sys
from collections import *
sys.setrecursionlimit(10**5)
itr = (line for line in sys.stdin.read().strip().split('\n'))
INP = lambda: next(itr)
def ni(): return int(INP())
def nl(): return [int(_) for _ in INP().split()]

import math

def solve(n,a):
    use = 10 - n
    return int((use * (use - 1)) * (1/2) * math.factorial(4) * (1/4))


t = ni()
for case in range(t):
    n = ni()
    a = nl()
    print(solve(n,a))
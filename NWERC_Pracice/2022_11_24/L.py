import sys
from collections import *
sys.setrecursionlimit(10**5)
itr = (line for line in sys.stdin.read().strip().split('\n'))
INP = lambda: next(itr)
def ni(): return int(INP())
def nl(): return [int(_) for _ in INP().split()]

import math

n = ni()

def solve(n):
    if n == 1: return 1
    if n == 2: return 0.5
    if n == 3: return 2/3
    if n <= 15:
        return 1 - math.floor(math.factorial(n) / math.e + 0.5) / math.factorial(n)
    
    return 1 - 1/math.e

print(solve(n))
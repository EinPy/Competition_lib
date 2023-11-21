import sys
from collections import *
sys.setrecursionlimit(10**5)
itr = (line for line in sys.stdin.read().strip().split('\n'))
INP = lambda: next(itr)
def ni(): return int(INP())
def nl(): return [int(_) for _ in INP().split()]

import math

def lcm ( a, b) :
    return a / math.gcd(a, b) * b


def solve(case):
    best = 10**6
    for s, a, b in case:
        merge = s + lcm(a, b)
        best = min(best, merge)
    print(int(best))
        
    return 0


t = ni()
cases = []
for c in range(t):
    cases.append(nl())
solve(cases)
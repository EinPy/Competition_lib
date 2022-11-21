import sys, math
from collections import *
sys.setrecursionlimit(10**5)
itr = (line for line in sys.stdin.read().strip().split('\n'))
INP = lambda: next(itr)
def ni(): return int(INP())
def nl(): return [int(_) for _ in INP().split()]



def solve():
    a, d = nl()

    n = a // math.gcd(a, d)
    d //= math.gcd(a, d)
    
    seen = {}
    left = n
    curr = 1
    while True:
        if left % d == 0:
            print(curr - 1, 0)
            return
        if (left, d) in seen:
            print(seen[(left, d)] - 2, curr - seen[(left, d)])
            return
        else:
            seen[(left, d)] = curr
            left = 10 * (left % d)
            curr += 1
solve()
        
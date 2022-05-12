import sys
from collections import *
sys.setrecursionlimit(10**5)
itr = (line for line in sys.stdin.read().strip().split('\n'))
INP = lambda: next(itr)
def ni(): return int(INP())
def nl(): return [int(_) for _ in INP().split()]



def f(x, a):
    return (x // a) + (x % a)


def solve(l, r , a):
    lower = r - (r % a) - 1
    if lower >= l:
        return max(f(r,a), f(lower, a))
    
    return f(r, a)
    

t = ni()
for case in range(t):
    l, r, c = nl()
    print(solve(l, r, c))
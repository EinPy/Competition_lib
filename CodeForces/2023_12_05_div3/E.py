import sys
from collections import *
sys.setrecursionlimit(10**5)
itr = (line for line in sys.stdin.read().strip().split('\n'))
INP = lambda: next(itr)
def ni(): return int(INP())
def nl(): return [int(_) for _ in INP().split()]

def ds(n):
    """Calculate the sum of the digits of a number."""
    return sum(map(int, str(n)))

def solve(n):

    cnt = 0
    for a in range(n+1):
        for b in range(n+1):
            for c in range(n+1):
                if a + b + c == n:
                    if ds(a) + ds(b) + ds(c) == ds(n):
                        cnt += 1
    print(f"{cnt},", end="")


for i in range(10):
    solve(i)
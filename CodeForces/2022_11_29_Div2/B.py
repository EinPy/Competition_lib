import sys
from collections import *
sys.setrecursionlimit(10**5)
itr = (line for line in sys.stdin.read().strip().split('\n'))
INP = lambda: next(itr)
def ni(): return int(INP())
def nl(): return [int(_) for _ in INP().split()]



def solve(n):
    if n == 1:
        print("1")
        return
    if n % 2 == 1:
        print("1 "*n)
        return
    out = []
    out.append(3)
    out.append(1)
    for el in range(n-2):out.append(2)
    print(' '.join(map(str,out)))

t = ni()
for case in range(t):
    n = ni()
    solve(n)
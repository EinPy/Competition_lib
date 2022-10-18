import sys
from collections import *
sys.setrecursionlimit(10**5)
itr = (line for line in sys.stdin.read().strip().split('\n'))
INP = lambda: next(itr)
def ni(): return int(INP())
def nl(): return [int(_) for _ in INP().split()]



t = ni()
for case in range(t):
    n = ni()
    out = [1]
    out.append(n)
    for i in range(2, n):
        out.append(i)
    print(' '.join(map(str,out)))
    
import sys
from collections import *
sys.setrecursionlimit(10**5)
itr = (line for line in sys.stdin.read().strip().split('\n'))
INP = lambda: next(itr)
def ni(): return int(INP())
def nl(): return [int(_) for _ in INP().split()]



t = ni()
for _ in range(t):
    a, b = nl()
    c, d = nl()
    if a == b == c == d == 0:
        print(0)
    elif a == b == c == d == 1:
        print(2)
    else:
        print(1)
        
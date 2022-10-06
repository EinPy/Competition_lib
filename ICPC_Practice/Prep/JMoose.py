import sys
from collections import *
sys.setrecursionlimit(10**5)
itr = (line for line in sys.stdin.read().strip().split('\n'))
INP = lambda: next(itr)
def ni(): return int(INP())
def nl(): return [int(_) for _ in INP().split()]



l, r =nl()
if l == r and l == 0:
    print("Not a moose")
elif l != r:
    print("Odd", max(l, r) * 2)
else:
    print("Even", l  + r)
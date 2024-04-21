import sys
from collections import *
sys.setrecursionlimit(10**5)
itr = (line for line in sys.stdin.read().strip().split('\n'))
INP = lambda: next(itr)
def ni(): return int(INP())
def nl(): return [int(_) for _ in INP().split()]


x=ni()
n = ni()
tot = 0
for i in range(n):
    tot+=ni()
print((1+n)*x - tot)
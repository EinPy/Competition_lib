import sys
from collections import *
sys.setrecursionlimit(10**5)
itr = (line for line in sys.stdin.read().strip().split('\n'))
INP = lambda: next(itr)
def ni(): return int(INP())
def nl(): return [int(_) for _ in INP().split()]



G, T, N = nl()
W = nl()
mid = G - T
Red = 0.9 * mid
Red -= sum(W)
print(int(Red))
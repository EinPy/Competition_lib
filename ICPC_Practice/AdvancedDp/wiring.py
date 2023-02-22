import sys
from collections import *
sys.setrecursionlimit(10**5)
itr = (line for line in sys.stdin.read().strip().split('\n'))
INP = lambda: next(itr)
def ni(): return int(INP())
def nl(): return [int(_) for _ in INP().split()]



def dp(i, remR, remB):
    if i == N:
        if remR == 0 and remB == 0:
            return 0
        else:
            return 10**18
    if isBlue(i):
        ans = dp(i+1, remR, remB + 1) + #...
    else:
        
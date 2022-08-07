import sys
from collections import *
sys.setrecursionlimit(10**5)
itr = (line for line in sys.stdin.read().strip().split('\n'))
INP = lambda: next(itr)
def ni(): return int(INP())
def nl(): return [int(_) for _ in INP().split()]



def solve(n,a):
    seen = {}
    for i in a:
        if i not in seen:
            seen[i] = 1
        else:
            seen[i] += 1
    #0 cannot change places
    #1 can only move closer to 0
    # each subsequent number can only 
            


t = ni()
for case in range(t):
    n = ni()
    a = nl()
    solve(n,a)
import sys
from collections import *
sys.setrecursionlimit(10**5)
itr = (line for line in sys.stdin.read().strip().split('\n'))
INP = lambda: next(itr)
def ni(): return int(INP())
def nl(): return [int(_) for _ in INP().split()]



def solve(n,tra):
    


t = ni()
tra = []
for case in range(t):
    l, r = nl()
    tra.append((l,r))
solve(t, tra)
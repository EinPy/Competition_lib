import sys
from collections import *
sys.setrecursionlimit(10**5)
itr = (line for line in sys.stdin.read().strip().split('\n'))
INP = lambda: next(itr)
def ni(): return int(INP())
def nl(): return [int(_) for _ in INP().split()]



def solve(n,m):
    dig = list(map(int,list(str(n))))
    print(n, dig)
        
    pass


t = ni()
for case in range(t):
    n,m = nl()
    solve(n,m)
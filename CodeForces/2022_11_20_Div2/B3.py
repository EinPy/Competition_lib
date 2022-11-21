import sys
from collections import *
sys.setrecursionlimit(10**5)
itr = (line for line in sys.stdin.read().strip().split('\n'))
INP = lambda: next(itr)
def ni(): return int(INP())
def nl(): return [int(_) for _ in INP().split()]



def solve(n,a):
    
    seen = {}
    for e in a:
        if e not in seen:
            seen[e] = 1
        
    #if only two elements 1 2 1 2 1 2
    #can do one 1 2 1 2
    #two 1 2
    u = len(seen.keys())
    if u == 2:
        print(1 + n // 2) # plus 1 for last two
    #if there is some element that there is only one of
    #it is always possible to use n operations
    else:
        print(n)
    

t = ni()
for case in range(t):
    n = ni()
    a = nl()
    solve(n,a)
import sys
from collections import *
sys.setrecursionlimit(10**5)
itr = (line for line in sys.stdin.read().strip().split('\n'))
INP = lambda: next(itr)
def ni(): return int(INP())
def nl(): return [int(_) for _ in INP().split()]





def solve(l,s):
    b, r, w = 0,0,0
    s = s.split('W')
#    print(s)
    for el in s:
        if len(el) == 1:
            return "NO"
        if len(el) != 0:
            if el.count("B") == 0 or el.count("R") == 0:
                return "NO"
        
    return "YES"

t = ni()
for c in range(t):
    l = ni()
    s = INP()
    print(solve(l,s))
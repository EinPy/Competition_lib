from functools import total_ordering
import sys
from collections import *
sys.setrecursionlimit(10**5)
itr = (line for line in sys.stdin.read().strip().split('\n'))
INP = lambda: next(itr)
def ni(): return int(INP())
def nl(): return [int(_) for _ in INP().split()]




import math
def solve(aa, t):
    if 'a' in t and len(t) != 1:
        return -1
    if t == 'a':
        return 1
    
    tot = 0
    for i in range(1, len(aa) + 1):
        tot += math.comb(len(aa),i)
    return tot + 1
        


t = ni()
for case in range(t):
    aaa = INP()
    t = INP()
    print(solve(aaa, t))
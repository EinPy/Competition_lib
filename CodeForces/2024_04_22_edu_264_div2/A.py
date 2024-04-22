import sys
from collections import *
sys.setrecursionlimit(10**5)
itr = (line for line in sys.stdin.read().strip().split('\n'))
INP = lambda: next(itr)
def ni(): return int(INP())
def nl(): return [int(_) for _ in INP().split()]




import math
t = ni()
for case in range(t):
    n,m,k = nl()
    big = math.ceil(n/m)
    if n - big <= k: 
        print("NO")
    else:
        print("YES")
        
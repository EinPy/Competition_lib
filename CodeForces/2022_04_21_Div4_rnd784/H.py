import sys
from collections import *
sys.setrecursionlimit(10**5)
itr = (line for line in sys.stdin.read().strip().split('\n'))
INP = lambda: next(itr)
def ni(): return int(INP())
def nl(): return [int(_) for _ in INP().split()]





def solve(n,k,arr):
    tot = arr[0]
    for n in arr:
        tot &= n
    print


t = ni()
for c in range(t):
    n,k = nl()
    arr = nl()
    solve(n,k,arr)
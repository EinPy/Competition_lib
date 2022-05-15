import sys
from collections import *
sys.setrecursionlimit(10**5)
itr = (line for line in sys.stdin.read().strip().split('\n'))
INP = lambda: next(itr)
def ni(): return int(INP())
def nl(): return [int(_) for _ in INP().split()]




def solve(a):
    l1, r1, l2, r2 = a
    
    arr1 = [i for i in range(l1, r1+1)]
    arr2 = [i for i in range(l2, r2+1)]
    
    for n in arr1:
        if n in arr2:
            return n
    return l1 + l2


t = ni()
for _ in range(t):
    a = nl()
    print(solve(a))
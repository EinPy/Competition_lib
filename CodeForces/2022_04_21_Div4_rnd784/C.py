import sys
from collections import *
sys.setrecursionlimit(10**5)
itr = (line for line in sys.stdin.read().strip().split('\n'))
INP = lambda: next(itr)
def ni(): return int(INP())
def nl(): return [int(_) for _ in INP().split()]





def solve(n,arr): 
    if n <= 2:
        return "YES"
    sameEvens, sameOdds = False, False
    e, o = arr[0] %2, arr[1] % 2
    
    
    for i in range(n):
        if i % 2 == 0:
            if arr[i] % 2 != e:
                return "NO"
        else:
            if arr[i] % 2 != o:
                return "NO"
    return "YES"





t = ni()
for i in range(t):
    l = ni()
    arr = nl()
    print(solve(l,arr))
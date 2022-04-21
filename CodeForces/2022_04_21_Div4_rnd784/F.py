import sys
from collections import *
sys.setrecursionlimit(10**5)
itr = (line for line in sys.stdin.read().strip().split('\n'))
INP = lambda: next(itr)
def ni(): return int(INP())
def nl(): return [int(_) for _ in INP().split()]





def solve(n,a):
    if n < 2:
        return 0
    
    ali = [0 for _ in range(n)]
    ali[0] = a[0]
    bob = [0 for _ in range(n)]
    bob[n-1] = a[n-1]
    
    for i in range(1,n):
        ali[i] = ali[i-1] + a[i]
    for j in range(n-2,-1,-1):
        bob[j] = bob[j+1] + a[j]
#    print(ali, bob)
    
    p1, p2 = 0, n-1
    best = 0
    while p1 < p2:
        if ali[p1] == bob[p2]:
            best = p1 + 1 + (n-p2 )
        if ali[p1] <= bob[p2]:
            p1 += 1
        else:
            p2 -= 1
    return best
    
    
t = ni()
for c in range(t):
    n = ni()
    a = nl()
    print(solve(n,a))
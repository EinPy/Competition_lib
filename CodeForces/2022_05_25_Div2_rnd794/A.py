import sys
from collections import *
sys.setrecursionlimit(10**5)
itr = (line for line in sys.stdin.read().strip().split('\n'))
INP = lambda: next(itr)
def ni(): return int(INP())
def nl(): return [int(_) for _ in INP().split()]



def solve(n,a):
    if len(set(a)) == 1:
        return "YES"
    tot = sum(a)
    for i in range(n):
        if (tot - a[i]) / (n-1) == a[i]:
            #print(tot - a[i], n-1, i)
            return "YES"
    return "NO"

t = ni()
for case in range(t):
    n = ni()
    a = nl()
    print(solve(n,a))
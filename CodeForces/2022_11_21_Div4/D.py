import sys
from collections import *
sys.setrecursionlimit(10**5)
itr = (line for line in sys.stdin.read().strip().split('\n'))
INP = lambda: next(itr)
def ni(): return int(INP())
def nl(): return [int(_) for _ in INP().split()]



def solve(n,a):
    isIncreasing = False
    if n == 1:
        print("YES")
        return
    for i in range(n-1):
        if a[i+1] > a[i]:
            isIncreasing = True
        if isIncreasing:
            if a[i+1] < a[i]:
                print("NO")
                return
    print("YES")
        

t = ni()
for case in range(t):
    n = ni()
    a = nl()
    solve(n,a)
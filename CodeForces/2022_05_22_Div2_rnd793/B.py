import sys
from collections import *
sys.setrecursionlimit(10**5)
itr = (line for line in sys.stdin.read().strip().split('\n'))
INP = lambda: next(itr)
def ni(): return int(INP())
def nl(): return [int(_) for _ in INP().split()]


def solve(n,a):
    orgA = a[:]
    a.sort()
    #print(orgA, a)
    num = None

    for i in range(n):
        if orgA[i] != a[i]:
            if num != None:
                num = num & i
            else:
                num = i
    
    print(num)


t = ni()
for case in range(t):
    n = ni()
    a = nl()
    solve(n,a)
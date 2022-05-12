import sys
from collections import *
sys.setrecursionlimit(10**5)
itr = (line for line in sys.stdin.read().strip().split('\n'))
INP = lambda: next(itr)
def ni(): return int(INP())
def nl(): return [int(_) for _ in INP().split()]





def solve(n, a):
    neg = 0
    for i in range(n):
        if a[i] < 0:
            neg += 1
            a[i] = a[i] * -1

    if neg == 0:
        for i in range(n-1):
            if a[i] > a[i+1]:
                return "NO"
        return "YES"

    for i in range(neg-1):
        if a[i+1] > a[i]:
            return "NO"

    for i in range(neg, n-1):
        if a[i] > a[i+1]:
            return "NO"

    return  "YES"




t = ni()

for _ in range(t):
    n = ni()
    a = nl()
    print(solve(n,a))
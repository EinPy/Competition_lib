import sys
from collections import *
sys.setrecursionlimit(10**5)
itr = (line for line in sys.stdin.read().strip().split('\n'))
INP = lambda: next(itr)
def ni(): return int(INP())
def nl(): return [int(_) for _ in INP().split()]



def solve(n,a):
    pass


t = ni()
for case in range(t):
    n, a, b = nl()
    if a == n and b == n:
        print("Yes")
    else:
        if a + b > n-2: 
            print("No")
        else:
            print("Yes")
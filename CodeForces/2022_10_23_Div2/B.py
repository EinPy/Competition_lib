import sys
from collections import *
sys.setrecursionlimit(10**5)
itr = (line for line in sys.stdin.read().strip().split('\n'))
INP = lambda: next(itr)
def ni(): return int(INP())
def nl(): return [int(_) for _ in INP().split()]



def solve(n):
    #maximum minimum diffrence between consequtive numbers
    #divide arreay into three?
    diff = n // 2
    out = []
    for i in range(1,n//2+1):
        out.append(i+diff)
        out.append(i)

    if n // 2 != n/2:
        out = [n] + out
    print(' '.join(map(str,out)))


t = ni()
for case in range(t):
    n = ni()
    solve(n)
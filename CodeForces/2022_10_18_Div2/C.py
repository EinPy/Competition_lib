import sys
from collections import *
sys.setrecursionlimit(10**5)
itr = (line for line in sys.stdin.read().strip().split('\n'))
INP = lambda: next(itr)
def ni(): return int(INP())
def nl(): return [int(_) for _ in INP().split()]



def solve(n,a,c):
    a = a + a
    a = list(a)
    #print(n,a,c)
    if c == 'g':
        print(0)
        return
    best = 0
    cur = 0
    s = False
    for i in a:
        if i == c:
            s = True
        if s:
            if i != 'g':
                cur += 1
            else:
                best = max(cur, best)
                cur = 0
                s = False
    print(best)


t = ni()
for case in range(t):
    n, c = INP().split()
    a = INP()
    solve(n,a,c)
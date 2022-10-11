import sys
from collections import *
sys.setrecursionlimit(10**5)
itr = (line for line in sys.stdin.read().strip().split('\n'))
INP = lambda: next(itr)
def ni(): return int(INP())
def nl(): return [int(_) for _ in INP().split()]



def solve(a):
    if a == 1 or a == 3:
        print(-1)
        return
    out = []
    out.append(a)
    out.append(a-1)
    for i in range(1,a-1):
        out.append(i)
    print(" ".join(list(map(str,out))))
        

t = ni()
for case in range(t):
    a = ni()
    solve(a)
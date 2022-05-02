import sys
from collections import *
sys.setrecursionlimit(10**5)
itr = (line for line in sys.stdin.read().strip().split('\n'))
INP = lambda: next(itr)
def ni(): return int(INP())
def nl(): return [int(_) for _ in INP().split()]

import math


def solve(x,y):
    if x > y and y != 0:
        print("0 0")
        return
    if x == y:
        print("1 1")
        return
    if y == 0:
        print("1 0")
        return 
    if x == 0:
        print("0 0")
        return

    for b in range(2,101):
        ans = math.log(y/x)/math.log(b)
        if ans == round(ans):
            print(f"{int(ans)} {int(b)}")
            return
        
    print("0 0")
    return

t = ni()
for case in range(t):
    a, b = nl()
    solve(a,b)
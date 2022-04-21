import sys
from collections import *
sys.setrecursionlimit(10**5)
itr = (line for line in sys.stdin.read().strip().split('\n'))
INP = lambda: next(itr)
def ni(): return int(INP())
def nl(): return [int(_) for _ in INP().split()]





def solve(a):
    if a < 1400:
        print("Division 4")
        return
    if a <1600:
        print("Division 3")
        return
    if a < 1900:
        print("Division 2")
        return
    else:
        print("Division 1")
        return
    
    



t = ni()
for i in range(t):
    a = ni()
    solve(a)
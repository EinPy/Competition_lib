import sys
from collections import *
sys.setrecursionlimit(10**5)
itr = (line for line in sys.stdin.read().strip().split('\n'))
INP = lambda: next(itr)
def ni(): return int(INP())
def nl(): return [int(_) for _ in INP().split()]



def solve(n,a):
    doub = len(a) - len(set(a))
    #will always get the amount of double cards I have
    #If more than half of double cards, will get n points, else only doub
    if doub > n // 2:
        print(n)
    else:
        print(doub)

t = ni()
for case in range(t):
    n = ni()
    a = nl()
    solve(n,a)
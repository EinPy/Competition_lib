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
    n = ni()
    a = nl()
    comp = a[:]
    comp.sort()
    out = []
    #print(comp)
    for s in a:
        if s != comp[-1]:
            out.append(s - comp[-1])
        else:
            out.append(s - comp[-2])
    print(" ".join(map(str,out)))
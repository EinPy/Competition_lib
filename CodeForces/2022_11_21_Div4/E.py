import sys
from collections import *
sys.setrecursionlimit(10**5)
itr = (line for line in sys.stdin.read().strip().split('\n'))
INP = lambda: next(itr)
def ni(): return int(INP())
def nl(): return [int(_) for _ in INP().split()]



def solve(n,a):
    c = 0
    o = 0
    pref = []
    #count first
    for i in range(n):
        if a[i] == 1:
            o += 1
        else:
            c += o
        pref.append(o)
    #make first 0 to a 1 or make last 1 to a 0
    first = False
    c2 = 0
    o = 0
    #case first 0 to one
    for i in range(n):
        if a[i] == 1:
            o += 1
        else:
            if not first:
                o += 1
                first = True
            else:
                c2 += o
    c3 = 0
    o = 0
    for i in range(n):
        if a[i] == 1:
            o += 1
        else:
            if not first:
                o += 1
                first = True
            else:
                c2 += o
            
        
        
        


t = ni()
for case in range(t):
    n = ni()
    a = nl()
    solve(n,a)
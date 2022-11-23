import sys
from collections import *
sys.setrecursionlimit(10**5)
itr = (line for line in sys.stdin.read().strip().split('\n'))
INP = lambda: next(itr)
def ni(): return int(INP())
def nl(): return [int(_) for _ in INP().split()]



def solve(n,a):
    p = []
    c = 0
    for e in a:
        c += e
        p.append(e)
    suff = []
    c = 0
    for i in range(n-1,-1,-1):
        c += a[i]
        suff.append(c)
    suff.reverse()
    #simply flip last 1 to a 0'
    c = 0
    inv = 0
    last1 = 0
    first0 = -1
    for i in range(n):
        c += a[i]
        if a[i] == 0:
            inv += c
            if first0 == -1:
                first0 = i
        else:
            last1 = i
    #two cases
    a1 =a[:]
    if first0 != -1:
        a1[first0] = 1
    else:
        a1[0] = 1
        
    c = 0
    inv2 = 0
    last1 = 0
    first0 = -1
    for i in range(n):
        c += a1[i]
        if a1[i] == 0:
            inv2 += c
            if first0 == -1:
                first0 = i
        else:
            last1 = i
            
    a2 = a[:]
    if last1 != 0:
        a2[last1] = 0
    
    c = 0
    inv3 = 0
    last1 = 0
    first0 = -1
    for i in range(n):
        c += a2[i]
        if a2[i] == 0:
            inv3 += c
            if first0 == -1:
                first0 = i
        else:
            last1 = i
    
    print(max(inv,inv2, inv3))
        
        
        


t = ni()
for case in range(t):
    n = ni()
    a = nl()
    solve(n,a)
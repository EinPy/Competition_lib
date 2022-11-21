from re import L
import sys
from collections import *
sys.setrecursionlimit(10**5)
itr = (line for line in sys.stdin.read().strip().split('\n'))
INP = lambda: next(itr)
def ni(): return int(INP())
def nl(): return [int(_) for _ in INP().split()]



def solve(n,a):
    if n == 1:
        print(-1)
        return
    m, p = a.count(-1), a.count(1)
    #print(a, m, p)
    if m == p:
        print(n)
        out = [[i+1,i+1] for i in range(n)]
        for a, b in out:
            print(a, b)
        #print(" ".join(map(str,out)))
    #two segments with sum 0
    T = p - m
    #key insight, younver need to make a subsegment longer than 2
    #if tot is negative we need to increase it
    out = []
    if T < 0:
        i = 0
        while i < n:
            #only way to increase is to createa segment of [1,  -1] to increase by one
            #or [-1,-1] to increase by one
            if T< 0 and i+1 < n and a[i+1] == -1 :
                out.append([i+1,i+2])
                T += 2
                i += 2
            else:
                out.append([i+1,i+1])
                i += 1
        if T == 0:
            print(len(out))
            for l, r in out:
                print(l, r)
        else:
            print(-1)
        return
                
    #if tot is positivewe ne
    if T > 0:
        #print(T, a)
        i = 0
        while i < n:
            #only way to decrease is to make [-1, 1] or [1, 1]
            if T >0 and i + 1 < n and a[i+1] == 1:
                out.append([i+1,i+2])
                T -= 2
                i += 2
            else:
                out.append([i+1,i+1])
                i += 1
        #print(out)
        if T == 0:
            print(len(out))
            for l, r in out:
                print(l, r)
        else:
            print(-1)
        return

t = ni()
for case in range(t):
    n = ni()
    a = nl()
    solve(n,a)
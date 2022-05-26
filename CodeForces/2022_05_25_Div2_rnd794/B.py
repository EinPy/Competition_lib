import sys
from collections import *
sys.setrecursionlimit(10**5)
itr = (line for line in sys.stdin.read().strip().split('\n'))
INP = lambda: next(itr)
def ni(): return int(INP())
def nl(): return [int(_) for _ in INP().split()]



def solve(n,a):
    #never want one longer than 2
    if n == 1:
        return 0
    if n == 2:
        if a[1] < a[0]:
            return 1
        else:
            return 0
        
    if n == 3:
        inv = 0
        f, s, l = a[0], a[1], a[2]
        if f > s:
            inv += 1
        if f > l:
            inv += 1
        if s > l:
            inv += 1
        if inv % 2 == 1:
            return 1
        else:
            return 0
    
    odss = 0
    curMax = 0
    i = 0
    curInv = 0
    while i <= n-3:
        
        curMax = max(curMax, a[i])
        if i != 1 and i != n-3:
            if a[i+1] < curMax:
                #print(i)
                odss += 1
                i += 1
                curMax = 0
        #edge cases
        if i == 1:
            inv = 0
            f, s, l = a[0], a[i], a[i+1]
            if f > s:
                inv += 1
            if f > l:
                inv += 1
            if s > l:
                inv += 1
            if inv % 2 == 1:
                odss += 1
                i += 1
                curMax = 0
                
        if i == n-3:
            inv = 0
            f, s, l = a[i], a[i+1], a[i+2]
            if f > s:
                inv += 1
            if f > l:
                inv += 1
            if s > l:
                inv += 1
            if inv % 2 == 1:
                odss += 1
                i += 1
                curMax = 0
            
        i += 1
        
    return odss

        


t = ni()
for case in range(t):
    n = ni()
    a = nl()
    print(solve(n,a))
import sys
from collections import *
sys.setrecursionlimit(10**5)
itr = (line for line in sys.stdin.read().strip().split('\n'))
INP = lambda: next(itr)
def ni(): return int(INP())
def nl(): return [int(_) for _ in INP().split()]





def solve(n,a):
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
        
    #real code
    
    i = 0
    curMax = 0
    inv = 0
    streak = 0
    tri = False
    do = False
    add = False
    while i < n:
        add = False
        tri = False
        do = False
        if i < n - 2:
            tri = tripCheck(n, a, i)
        if i < n - 1:
            do = dubCheck(n, a, i)
        if streak != 1:
            if i + 2 != n -1:
                if do:
                    i += 2
                    add = True
                    streak = 0
                    inv += 1
                    print("here")
            if i + 3 != n-1 and not add:
                if tri:
                    print("tri", i)
                    i += 3
                    add = True
                    streak = 0
                    inv += 1
                    
        if not add:
            i += 1
            streak += 1
                
    return inv
    
                    
            

def tripCheck(n,a,i):
    inv = 0
    f, s, l = a[i], a[i+1], a[i+2]
    if f > s:
        inv += 1
    if f > l:
        inv += 1
    if s > l:
        inv += 1
    if inv % 2 == 1:
        return 1
    return 0

def dubCheck(n, a, i):
    inv = 0
    f, s= a[i], a[i+1]
    if f > s:
        return 1
    return 0



t = ni()
for case in range(t):
    n = ni()
    a = nl()
    print(solve(n,a))
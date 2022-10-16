import sys
from collections import *
sys.setrecursionlimit(10**5)
itr = (line for line in sys.stdin.read().strip().split('\n'))
INP = lambda: next(itr)
def ni(): return int(INP())
def nl(): return [int(_) for _ in INP().split()]



def solve(n,a):
    e = 0
    #amount of factors of two
    d = {}
    for i in range(1,32):
        d[2**i] = i
    div = list(d.keys())
    
    #print(div)
    
    for i in a:
        if i % 2 == 0:
            best = 2
            for num in div:
                if i % num == 0:
                    best = num
            e += d[best]
    #print("f", e)
    if e >= n:
        print(0)
        return
    add = 0
    fa = []
    for i in range(n,0, -1):
        if i % 2 == 0:
            best = 2
            for num in div:
                if i % num == 0:
                    best = num
            fa.append(d[best])
        
    fa.sort(reverse=True)
    for i in fa:
        e += i
        add += 1
        if e >= n:
                print(add)
                return
    print(-1)
    return



t = ni()
for case in range(t):
    n = ni()
    a = nl()
    solve(n,a)
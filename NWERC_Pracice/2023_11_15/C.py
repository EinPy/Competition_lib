
import sys
from collections import *
sys.setrecursionlimit(10**5)
itr = (line for line in sys.stdin.read().strip().split('\n'))
INP = lambda: next(itr)
def ni(): return int(INP())
def nl(): return [float(_) for _ in INP().split()]



def bns(targ):


    return -1


def solve(s, x, y):
    #binary search speed
    l, r = 0, 10**8
    neg = False
    if x < 0:
        neg = True
    x = abs(x)
    #vertical speed 1 km/min
    #total shield area
    tots = 0
    for low, h, f in s:
        tots += h - low
    non_shield = y - tots
    
    mid = 0
    for rep in range(60):
        mid = (l + r) / 2
        final_x = 0
        for low, h, f in s:
            final_x += (h-low) * mid * f
        final_x += non_shield * mid
        #print(final_x, x)
        #print(l, r ,mid, final_x, x)
        if final_x > x:
            r = mid
        else:
            l = mid
    
    if neg:
        return -1 *  mid
    return mid

x, y = nl()
n = ni()

shld = []
for _ in range(n):
    shld.append(nl())
    
    
print(solve(shld, x, y))
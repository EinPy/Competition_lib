from re import U
import sys
from collections import *
sys.setrecursionlimit(10**5)
itr = (line for line in sys.stdin.read().strip().split('\n'))
INP = lambda: next(itr)
def ni(): return int(INP())
def nl(): return [int(_) for _ in INP().split()]



def solve(n, a):
    x, y = 0, 0
    seen = {}
    dist = 1e6
    l, r = -1, -1
    seen[(0,0)] = 0
    #print(x,y)
    for i, s in enumerate(a):
        if s == "U":
            y += 1
        if s == "D":
            y -= 1
        if s == "L":
            x -= 1
        if s == "R":
            x += 1
        #print(x,y)
        if (x,y) in seen:
            if i - seen[(x,y)] < dist:
                dist = i - seen[(x,y)]
                l = seen[(x,y)]
                r = i

                    
        seen[(x,y)] = i + 1
            
    if dist != 1e6:
        print(l +1, r+ 1)
    else:print(-1)
    


t = ni()
for case in range(t):
    n = ni()
    a = list(INP())
    solve(n, a)
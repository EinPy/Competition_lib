import sys
from collections import *
sys.setrecursionlimit(10**5)
itr = (line for line in sys.stdin.read().strip().split('\n'))
INP = lambda: next(itr)
def ni(): return int(INP())
def nl(): return [int(_) for _ in INP().split()]

import random

def pts2line(p, q):
    return (-q[1] + p[1],
          q[0] - p[0],
          p[0]*q[1] - p[1]*q[0])


n = ni()
p = ni()
pts = []
for _ in range(n):
    pts.append(nl())
if n == 1:
    print("possible")
else:
    found = False 
    if n > 100:
        for N in range(500):
            x, y = random.randint(0,n-1), random.randint(0, n-1)
            if x != y:
                a, b, c = pts2line(pts[x], pts[y])
                cnt = 2
                for i in range(n):
                    if i != x and i != y:
                        x1, y1 = pts[i][0], pts[i][1]
                        if a * x1 + b * y1 + c == 0:
                            cnt += 1
                if cnt >= math.ceil(n * p / 100):
                    found = True
                    break
        
    if found:
        print("possible")
    else:
        print("impossible")
import sys
from collections import *
sys.setrecursionlimit(10**5)
itr = (line for line in sys.stdin.read().strip().split('\n'))
INP = lambda: next(itr)
def ni(): return int(INP())
def nl(): return [float(_) for _ in INP().split()]

import math as m
R = 1

def xyz(f):
    phi, the = f
    return (R * m.sin(phi) * m.cos(the),
            R * m.sin(phi) * m.sin(the),
            R * m.cos(phi)
            )

def dot(A, B):
    return A[0]*B[0] + A[1] * B[1] + A[2] * B[2]

def sz(A):
    return m.sqrt(A[0]**2 + A[1] ** 2 + A[2] ** 2)

def anglebetween(A, B):
    return m.acos( dot(A, B) / (sz(A) * sz(B)))

while True:
    try:
        n = ni()
        pts = []
        for _ in range(n):
            phi, theta = nl()
            
            pts.append((phi * (2*m.pi) /360 , theta * (2*m.pi) /360 ))
            
        curmax = 1000000000
        bestpnt = (0,0)
        for i in range(len(pts)):
            curcur = 10000000000
            for j in range(i+1, len(pts)):
                vecA = xyz(pts[i])
                vecB = xyz(pts[j])
                the = anglebetween(vecA, vecB)
                if the <= curcur:
                    curcur = the
            if curcur <= curmax:
                curmax = curcur
                bestpnt = pts[i]
        #print((bestpnt[0] * (2*m.pi / 360)), bestpnt[1] * (2*m.pi / 360))
        print("{:.2f}".format(bestpnt[0]* (2*m.pi / 360)), end= " ")
        print("{:.2f}".format(bestpnt[1]* (2*m.pi / 360)))

    except:
        exit()
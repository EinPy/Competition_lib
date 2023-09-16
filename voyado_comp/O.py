import sys
from collections import *
sys.setrecursionlimit(10**5)
itr = (line for line in sys.stdin.read().strip().split('\n'))
INP = lambda: next(itr)
def ni(): return int(INP())
def nl(): return [float(_) for _ in INP().split()]

import math

def compute(a, b, t):
    return (a**2 * t**3)/(24 * math.pi**2) + (a * t**2 * b)/(4 * math.pi) + (b**2 * t) / 2

def find_area(a, b, t1, t2):

    return compute(a, b, t2) - compute(a, b, t1)
    
def find_angles(start, r, area, a, b, num):
    l = 0
    mid = (l + r) / 2
    calc = find_area(a, b,0, mid)
    targ = num * area
    t = 0
    while t < 30:
        t += 1
        #print("here")
        if targ - calc > 0:
            l = mid
        elif targ - calc < 0:
            r = mid
        else:
            return mid
        mid = (l + r) / 2
        calc = find_area(a, b,0, mid)
        
    return mid

def solve():
    a, b, N = nl()
    #print(a, b, N)
    totA = find_area(a, b, 0, 2 * math.pi)
    slice = totA / N
    angles = []
    start = 0
    for s in range(int(N-1)):
        cut = find_angles(start, 4 * math.pi, slice, a, b, s + 1)
        start = cut
        angles.append(cut)
    for a in angles:
        print('{0:.10f}'.format(a))
    # print('\n'.join(map(str, angles)))



solve()
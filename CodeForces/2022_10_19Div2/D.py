import sys
from collections import *
sys.setrecursionlimit(10**5)
itr = (line for line in sys.stdin.read().strip().split('\n'))
INP = lambda: next(itr)
def ni(): return int(INP())
def nl(): return [int(_) for _ in INP().split()]

import random

n = ni()
#a = INP()
a = []
for _ in range(1000000):
    a.append(random.randint(0,1))
a += [0] * 500000
a.append(1)
a += [0] * 500000
a = ''.join(map(str,a))
n = len(a)
if a.count("1") == 0:
    print(0)
else:
    f = False
    f0 = False
    first = 0
    f0i = 0
    for i in range(n):
        if a[i] == "1":
            if not f:
                f = True
                first = i
        if f:
            if a[i] == "0":
                if not f0:
                    f0 = True
                    f0i = i
    l = n - f0i
    #print(l)
    org = int(a[first:],2)
    best = int(a[first:],2)
    for i in range(n-l+1):
        #print(int(a[i:i+l],2))
        best = max(best, org | int(a[i:i+l],2))
    print(bin(best)[2:])
    #now hopefully find substring of n - f0i length
            

#always want the first 1 to be included
#maximize leading ones

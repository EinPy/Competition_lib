import sys
from collections import *
sys.setrecursionlimit(10**5)
itr = (line for line in sys.stdin.read().strip().split('\n'))
INP = lambda: next(itr)
def ni(): return int(INP())
def nl(): return [int(_) for _ in INP().split()]


t = ni()
for case in range(t):
    n, q = nl()
    a = nl()
    oddS, eveS = 0, 0
    tot = 0
    for i in a:
        tot += i
        if i % 2 == 0:
            eveS += 1
        else:
            oddS += 1
    for _ in range(q):
        a, b = nl()
        if a == 0: 
            tot += b * eveS
            if b % 2 != 0:
                oddS += eveS
                eveS = 0
        else:
            tot += b * oddS
            if b % 2 != 0:
                eveS += oddS
                oddS = 0
        print(tot)
    #a = nl()
    #solve(n,a)
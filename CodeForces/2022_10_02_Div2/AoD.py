import sys
from collections import *
sys.setrecursionlimit(10**5)
itr = (line for line in sys.stdin.read().strip().split('\n'))
INP = lambda: next(itr)
def ni(): return int(INP())
def nl(): return [int(_) for _ in INP().split()]



n = ni()
a = nl()
pos = False
def solve():
    global pos
    global n
    global a
    for i in range(0, n-1):
        l1 = list(str(a[i]))
        l2 = list(str(a[i+1]))
        
        if len(l2) == 1:
            if a[i] != 0:
                pos = True
                a[i+1] = 0
                return
            
        for j in range(len(l1)):
            lB = l1[:]
            lB[j] = '9'
            lS = l2[:]
            if j != 0:
                lS[j] = '0'
            else:
                lS[j] = '1'
            if int(''.join(lB)) > a[i+1]:
                pos = True
                a[i] = int(''.join(lB))
                return
            if int(''.join(lS)) < a[i]:
                pos = True
                a[i+1] = int(''.join(lS))
                return
solve()
if pos:
    for n in a:
        print(n, end = " ")
else:
    print("impossible")
        
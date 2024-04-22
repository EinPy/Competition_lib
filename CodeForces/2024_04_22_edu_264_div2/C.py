import sys
from collections import *
sys.setrecursionlimit(10**5)
itr = (line for line in sys.stdin.read().strip().split('\n'))
INP = lambda: next(itr)
def ni(): return int(INP())
def nl(): return [int(_) for _ in INP().split()]



def solve(n,a):
    pass


t = ni()
for case in range(t):
    #take the first biggest digit into one of the numbers, then smallest?
    a = list(map(int,list(INP())))
    b = list(map(int,list(INP())))
    p = 0
    for i in range(len(a)):
        if not p:
            if a[i] != b[i]:
                a[i],b[i] = max(a[i],b[i]), min(a[i],b[i])
                p = 1
        else:
            a[i],b[i] = min(a[i],b[i]), max(a[i],b[i])
    print(''.join(map(str,a)))
    print(''.join(map(str,b)))
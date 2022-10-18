import sys
from collections import *
sys.setrecursionlimit(10**5)
itr = (line for line in sys.stdin.read().strip().split('\n'))
INP = lambda: next(itr)
def ni(): return int(INP())
def nl(): return [int(_) for _ in INP().split()]



def solve(n, a, s):
    s = list(map(int,list(s)))
    #print(s)
    tot = 0
    rem = [False for _ in range(n)]
    for i in range(n-1):
        #print(i, end = " ")
        added = False
        if i == 0:
            if s[i] == 1:
                tot += a[i]
                added = True
        if not added:
            if a[i] >= a[i+1] and (rem[i] or s[i] == 0) and s[i+1] == 1:
                #print(" this one ", end=" ")
                rem[i+1] = True
                tot += a[i]
            if s[i] == 1 and not rem[i]:
                #print("here", end = " ")
                tot += a[i]
        #print(tot)
    print(tot)
            

t = ni()
for case in range(t):
    n = ni()
    s = INP()
    a = nl()
    solve(n, a, s)
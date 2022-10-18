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
    #greedy failed
    #for each segment of ones, excluding 0, you can choose the n-1 largest
    i = 0
    l = 0
    curS, curM = 0, 1e9
    segs = []
    streak = False
    for i in range(n):
        if s[i] == 1:
            if not streak:
                l = i
            streak = True
        if s[i] == 0 and streak:
            segs.append([l,i-1])
            streak = False
    if streak:
        segs.append([l, n-1])
    
    for x, y in segs:
        if x == 0:
            for i in range(x, y+1):
                tot += a[i]
        else:
            m = 1e9
            for i in range(x-1, y+1):
                tot += a[i]
                m = min(m, a[i])
            tot -= m
        
    print(tot)
            

t = ni()
for case in range(t):
    n = ni()
    s = INP()
    a = nl()
    solve(n, a, s)
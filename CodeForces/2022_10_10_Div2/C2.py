import sys
from collections import *
sys.setrecursionlimit(10**5)
itr = (line for line in sys.stdin.read().strip().split('\n'))
INP = lambda: next(itr)
def ni(): return int(INP())
def nl(): return [int(_) for _ in INP().split()]



def solve(n,a):
    best = n
    for i in range(n):
        targ = sum(a[:i+1])
        #print(targ)
        tot = 0
        lStreak = i+1
        streak = 0
        long = 0
        pos = True
        for j in range(i+1, n):
            tot += a[j]
            streak += 1
            if tot > targ:
                pos = False
                break
            if tot == targ:
                lStreak = max(streak, lStreak)
                streak = 0
                tot = 0
        if tot != 0:
            pos = False
        #print(pos, i, targ, lStreak)
        if pos:
            best = min(lStreak, best)
           # print("best is now", best)
    print(best)

t = ni()
for case in range(t):
    n = ni()
    a = nl()
    solve(n,a)
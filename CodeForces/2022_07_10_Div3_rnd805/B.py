import sys
from collections import *
sys.setrecursionlimit(10**5)
itr = (line for line in sys.stdin.read().strip().split('\n'))
INP = lambda: next(itr)
def ni(): return int(INP())
def nl(): return [int(_) for _ in INP().split()]



def solve(a):
    days = 1
    seen = {}
    cnt = 0
    for i in range(len(a)):
        if a[i] not in seen:
            seen[a[i]] = True
            cnt += 1
        if cnt == 4:
            days += 1
            cnt = 1
            seen = {a[i] : True}
    print(days)
            
        


t = ni()
for case in range(t):
    a = INP()
    solve(a)
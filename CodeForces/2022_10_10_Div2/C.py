import sys
from collections import *
sys.setrecursionlimit(10**5)
itr = (line for line in sys.stdin.read().strip().split('\n'))
INP = lambda: next(itr)
def ni(): return int(INP())
def nl(): return [int(_) for _ in INP().split()]



def solve(n,a):
    good = False
    maxlens = [] * n
    possible = 0
    i = 0
    streak = 1
    j = 1
    while i < n:
        while j < n and a[j] >= j - i + 1 :
            streak += 1
            j += 1
        #print(i, j, streak)
        possible += streak
        i += 1
        streak -= 1
    print(int(possible))
        
            
        
        

t = ni()
for case in range(t):
    n = ni()
    a = nl()
    solve(n,a)
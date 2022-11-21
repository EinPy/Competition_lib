import sys
from collections import *
sys.setrecursionlimit(10**5)
itr = (line for line in sys.stdin.read().strip().split('\n'))
INP = lambda: next(itr)
def ni(): return int(INP())
def nl(): return [int(_) for _ in INP().split()]



def solve(n,a):
    seen = {}
    def rec(a, ops):
        if len(a) < 4:
            return len(a) + ops
        if tuple(a) in seen and seen[tuple(a)] >= ops:
            return seen[tuple(a)]
        best = 0
        for i in range(len(a)):
            new = a[:]
            if i == 0:
                new.pop(0)
                if new[0] == new[-1]:
                    new.pop(-1)
            elif i == len(new)-1:
                new.pop(-1)
                if new[0] == new[-1]:
                    new.pop(-1)
            else:
                new.pop(i)
                if new[i-1] == new[i]:
                    new.pop(i)
            ans = rec(new,ops+1)
            best = max(best, ans)
            seen[tuple(new)] = ans
        return best
    print(rec(a,0))
        
                

t = ni()
for case in range(t):
    n = ni()
    a = nl()
    solve(n,a)
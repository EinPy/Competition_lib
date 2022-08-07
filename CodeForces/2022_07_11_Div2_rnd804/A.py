import sys
from collections import *
sys.setrecursionlimit(10**5)
itr = (line for line in sys.stdin.read().strip().split('\n'))
INP = lambda: next(itr)
def ni(): return int(INP())
def nl(): return [int(_) for _ in INP().split()]



def solve(n):
    bin = format(n,"b")
    # a or b + b or c + a or c
    even = False
    if n % 2 == 0: even = True
    
    if not even:
        print(-1)
    else:
        a, b, c = 0, 0,0
        a = n//2
        c = n//2
        print(f"{a} 0 {c}")
        
         


t = ni()
for case in range(t):
    n = ni()
    solve(n)
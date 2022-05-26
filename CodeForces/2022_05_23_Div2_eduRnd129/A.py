import sys
from collections import *
sys.setrecursionlimit(10**5)
itr = (line for line in sys.stdin.read().strip().split('\n'))
INP = lambda: next(itr)
def ni(): return int(INP())
def nl(): return [int(_) for _ in INP().split()]



def solve(n, a, m, b):
    ma, mb = max(a), max(b)
    
    if ma > mb:
        print("Alice")
        print("Alice")
    elif mb > ma:
        print("Bob")
        print("Bob")
    else:
        print("Alice")
        print("Bob")


t = ni()
for case in range(t):
    n = ni()
    a = nl()
    m = ni()
    b = nl()
    solve(n, a, m, b)
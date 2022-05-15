import sys
from collections import *
sys.setrecursionlimit(10**5)
itr = (line for line in sys.stdin.read().strip().split('\n'))
INP = lambda: next(itr)
def ni(): return int(INP())
def nl(): return [int(_) for _ in INP().split()]




def solve(a, b):
    mi, ma = min(a,b), max(a,b)
    if (mi + ma) % 3 == 0 and mi * 2 >= ma:
        print("YES")
    else: print("NO")


t = ni()
for case in range(t):
    a, b = nl()
    solve(a, b)
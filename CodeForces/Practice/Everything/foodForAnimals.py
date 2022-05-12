import sys
from collections import *
sys.setrecursionlimit(10**5)
itr = (line for line in sys.stdin.read().strip().split('\n'))
INP = lambda: next(itr)
def ni(): return int(INP())
def nl(): return [int(_) for _ in INP().split()]





def solve(arr):
    a, b, c, x , y = arr
    missing = 0
    missing += max(0, x - a)
    missing += max(0, y - b)
    if missing <= c:
        print("YES")
    else:
        print("NO")
    



t = ni()
for case in range(t):
    arr = nl()
    solve(arr)
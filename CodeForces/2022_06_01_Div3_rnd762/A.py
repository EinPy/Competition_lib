import sys
from collections import *
sys.setrecursionlimit(10**5)
itr = (line for line in sys.stdin.read().strip().split('\n'))
INP = lambda: next(itr)
def ni(): return int(INP())
def nl(): return [int(_) for _ in INP().split()]


t = ni()
for case in range(t):
    a = INP()
    if len(a) %2 != 0:
        print("NO")
    else:
        if a[:len(a)//2] == a[len(a)//2:]:
            print("YES")
        else:
            print("NO")

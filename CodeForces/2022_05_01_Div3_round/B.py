import sys
from collections import *
sys.setrecursionlimit(10**5)
itr = (line for line in sys.stdin.read().strip().split('\n'))
INP = lambda: next(itr)
def ni(): return int(INP())
def nl(): return [int(_) for _ in INP().split()]





def solve(a):
    w = 'abcdefghijklmnopqrstuvwxyz'
    first = w.index(a[0])
    second = w.index(a[1])
    if second < first:
        return first*25 + second + 1
    else:
        return first * 25 + second 


t = ni()
for case in range(t):
    w = INP()
    print(solve(w))
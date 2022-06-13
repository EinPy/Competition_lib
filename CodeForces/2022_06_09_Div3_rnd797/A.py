import sys
from collections import *
sys.setrecursionlimit(10**5)
itr = (line for line in sys.stdin.read().strip().split('\n'))
INP = lambda: next(itr)
def ni(): return int(INP())
def nl(): return [int(_) for _ in INP().split()]



def solve(a):
    #(x-1) + (x+1) + x = n
    # 3x = n
    # x = (n) / 3
    b = a % 3
    h = a // 3
    #print(b,h)
    if b == 0:
        print(h, h+1, h-1)
    elif b == 1:
        print(h, h+2, h-1)
    else:
        print(h+1, h+2, h-1)


t = ni()
for case in range(t):
    a = ni()
    solve(a)
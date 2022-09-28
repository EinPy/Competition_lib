import sys
from collections import *
sys.setrecursionlimit(10**5)
itr = (line for line in sys.stdin.read().strip().split('\n'))
INP = lambda: next(itr)
def ni(): return int(INP())
def nl(): return [int(_) for _ in INP().split()]



def solve(a, b):
    if a % 2 == 0:
        if b % 2 == 0:
            print("Tonya")
        else:
            print("Burenka")
    else:
        if b % 2 == 0:
            print("Burenka")
        else:
            print("Tonya")
            


t = ni()
for case in range(t):
    a, b = nl()
    solve(a, b)
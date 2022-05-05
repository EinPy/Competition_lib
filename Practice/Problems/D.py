import sys
from collections import *
sys.setrecursionlimit(10**5)
itr = (line for line in sys.stdin.read().strip().split('\n'))
INP = lambda: next(itr)
def ni(): return int(INP())
def nl(): return [int(_) for _ in INP().split()]





def solve(n, w):
    for i in range(0, n):
        c = n - i

        if c == 1:
            print(f"{c} bottle of {w} on the wall, {c} bottle of {w}. \nTake it down, pass it around, no more bottles of {w}.")
        elif c == 2:
            print(f"{c} bottles of {w} on the wall, {c} bottles of {w}. \nTake one down, pass it around, {c-1} bottle of {w} on the wall.")

        else:
            print(f"{c} bottles of {w} on the wall, {c} bottles of {w}. \nTake one down, pass it around, {c-1} bottles of {w} on the wall.")
            print()
        
n = ni()
w = INP()
solve(n, w)
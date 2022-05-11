import sys
from collections import *
sys.setrecursionlimit(10**5)
itr = (line for line in sys.stdin.read().strip().split('\n'))
INP = lambda: next(itr)
def ni(): return int(INP())
def nl(): return [int(_) for _ in INP().split()]





def solve(s, c):
    p = []
    for i in range(len(s)):
        if s[i] == c:
            if i % 2 == 0:
                return "YES"

    return "NO"



t = ni()
for case in range(t):
    s = INP()
    c = INP()
    print(solve(s, c))
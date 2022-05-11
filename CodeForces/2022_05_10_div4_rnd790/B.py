#To start code
import sys
from collections import *
sys.setrecursionlimit(10**5)
itr = (line for line in sys.stdin.read().strip().split('\n'))
INP = lambda: next(itr)
def ni(): return int(INP())
def nl(): return [int(_) for _ in INP().split()]


#code







def solve(n,a):
    m = min(a)
    eat = 0
    for i in range(n):
        eat += a[i] - m
    return eat




t = ni()
for case in range(t):
    n, m = nl()
    a = []
    for i in range(n):
        a.append(INP())
    print(solve(n,m,a))
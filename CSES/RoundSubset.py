import sys
from collections import *
sys.setrecursionlimit(10**5)
itr = (line for line in sys.stdin.read().strip().split('\n'))
INP = lambda: next(itr)
def ni(): return int(INP())
def nl(): return [int(_) for _ in INP().split()]


#solution to https://codeforces.com/contest/837/problem/D


n, k = nl()
nums = nl()
dp = [[0 for _ in range(k+1)] for _ in range(n+1)]

for nu in range(n+1):
    for amount in range(k):
        
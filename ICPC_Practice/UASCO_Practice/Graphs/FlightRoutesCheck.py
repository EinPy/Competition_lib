#solution to https://cses.fi/problemset/task/1682
import sys
from collections import *
sys.setrecursionlimit(10**5)
itr = (line for line in sys.stdin.read().strip().split('\n'))
INP = lambda: next(itr)
def ni(): return int(INP())
def nl(): return [int(_) for _ in INP().split()]



def solve(n, adj):
    pass


n, m = nl()
adj = [[] for i in range(n+1)]
for case in range(n):
    a,b  = nl()
    adj[a].append(b)
    
solve(n, adj)
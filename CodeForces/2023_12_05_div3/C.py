import sys
from collections import *
sys.setrecursionlimit(10**5)
itr = (line for line in sys.stdin.read().strip().split('\n'))
INP = lambda: next(itr)
def ni(): return int(INP())
def nl(): return [int(_) for _ in INP().split()]

from collections import deque

def solve(n,a):
    cnt = [0] * (ord('z') - ord('a') + 1)
    for i in range(len(a)):
        cnt[ord(a[i]) - ord('a')] += 1
    cnt.sort()
    maxrem = max(cnt[-1] - sum(cnt[:-1]), 0)
    if maxrem == 0 and len(a) % 2 == 1:
        maxrem += 1
    print(maxrem)
    


t = ni()
for case in range(t):
    n = ni()
    a = INP()
    solve(n,a)
    
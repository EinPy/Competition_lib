import sys
from collections import *
sys.setrecursionlimit(10**5)
itr = (line for line in sys.stdin.read().strip().split('\n'))
INP = lambda: next(itr)
def ni(): return int(INP())
def nl(): return [int(_) for _ in INP().split()]





def solve(n, k):
    #  N*((2A1+ (N-1)*D)/2).
    s = ['a'] * n
    for i in range(n - 2, -1, -1):
        if k <= n - i - 1:
            s[i] = 'b'
            s[n-k] = 'b'
            return ''.join(s)
        k -= n - i - 1


t = ni()

for case in range(t):
    n, k = nl()
    print(solve(n, k))
    
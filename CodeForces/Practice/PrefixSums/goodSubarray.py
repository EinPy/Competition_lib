import sys
from collections import *
sys.setrecursionlimit(10**5)
itr = (line for line in sys.stdin.read().strip().split('\n'))
INP = lambda: next(itr)
def ni(): return int(INP())
def nl(): return [int(_) for _ in INP().split()]


def solve(n,a):
    a = [int(_) for _ in str(a)] 
    #print(a)
    d = {0 : 1}
    s, result = 0,0

    for i in range(n):
        s += a[i]
        x = s - i - 1

        if x not in d:
            d[x] = 0
        d[x] += 1
        result += d[x] - 1

    print(result)


"""
t = ni()
for case in range(t):
    n = ni()
    a = ni()
    solve(n,a)
"""
solve(100000,'0' * 100000)
import sys
from collections import *
sys.setrecursionlimit(10**5)
itr = (line for line in sys.stdin.read().strip().split('\n'))
INP = lambda: next(itr)
def ni(): return int(INP())
def nl(): return [int(_) for _ in INP().split()]


def solve(n,a):
    if n == 2:
        return 2
    rem = 0
    if n % 2 == 0:
        #0 index
        n -= 1
        l, r = n //2, n // 2 + 1
        char = 0
        #print(l, r)
        if a[l] == a[r]:
            rem += 2
            char = a[l]
        while char:
            #print(l, r)
            if l-1 >= 0 and a[l-1] == char:
                l -= 1
                rem += 1
            elif r +1 <= n and a[r+1] == char:
                r += 1
                rem += 1
            else:
                break
    else:
        l , r = n //2, n // 2
        rem += 1
        char = a[l]
        n -= 1
        while char:
            if l-1 >= 0 and a[l-1] == char:
                l -= 1
                rem += 1
            elif r +1 <= n and a[r+1] == char:
                r += 1
                rem += 1
            else:
                break
    return rem
        



t = ni()
for case in range(t):
    n = ni()
    a = INP()
    print(solve(n,a))
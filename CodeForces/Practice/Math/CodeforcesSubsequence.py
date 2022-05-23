import sys
from collections import *
sys.setrecursionlimit(10**5)
itr = (line for line in sys.stdin.read().strip().split('\n'))
INP = lambda: next(itr)
def ni(): return int(INP())
def nl(): return [int(_) for _ in INP().split()]


def prod(a):
    t = 1
    for n in a:
        t *= n
    return t

def solve(n):
    s = "codeforces"
    if n == 1:
        return s
    arr = [0] * len(s)
    tot = 1
    while tot < n:
        for i in range(len(s)):
            arr[i] += 1
            tot= prod(arr)
            if tot >= n:
                break

    newS = ''
    for i in range(len(s)):
        newS += s[i] * arr[i]

    return newS


n = ni()
print(solve(n))
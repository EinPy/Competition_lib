import sys
from collections import *
sys.setrecursionlimit(10**5)
itr = (line for line in sys.stdin.read().strip().split('\n'))
INP = lambda: next(itr)
def ni(): return int(INP())
def nl(): return [int(_) for _ in INP().split()]





def solve(arr):
    hash = {}
    for a in arr:
        if a not in hash:
            hash[a] = 1
        else:
            hash[a] += 1
            if hash[a] >= 3:
                return a
    return -1



t = ni()
for i in range(t):
    l = ni()
    arr = nl()
    print(solve(arr))
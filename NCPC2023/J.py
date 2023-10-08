import sys
from collections import *
sys.setrecursionlimit(10**5)
itr = (line for line in sys.stdin.read().strip().split('\n'))
INP = lambda: next(itr)
def ni(): return int(INP())
def nl(): return [int(_) for _ in INP().split()]



n, m = nl()
arr = nl()
if m >= n:
    print(max(arr))
else:
    arr = sorted(arr)
    #print(arr)
    doub = n - m #has to carry 2
    #print(doub, arr[0], arr[0]+ arr[2 * doub - 1])
    sums = []
    for i in range(doub):
        sums.append(arr[i] + arr[doub * 2 - 1 - i])
    #print(sums)
    print(max(max(sums), max(arr)))
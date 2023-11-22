import sys
from collections import *
sys.setrecursionlimit(10**5)
itr = (line for line in sys.stdin.read().strip().split('\n'))
INP = lambda: next(itr)
def ni(): return int(INP())
def nl(): return [int(_) for _ in INP().split()]


n, c, b = nl()
b = nl()
zero = [False for _ in range(n)]
for idx in b:
    zero[idx-1] = True
bnr = [0 for _ in range(n)]
if c == 0:
    print("".join(map(str,bnr)))
else:
    if c % 2 == 0:
        #don't add the first
        idx = 1
        while c:
            if zero[idx]:
                idx += 1
            else:
                bnr[idx] = 1
                c -= 2
                idx += 2
    else:
        bnr[0] = 1
        c -= 1
        idx = 2
        while c:
            if zero[idx]:
                idx += 1
            else:
                bnr[idx] = 1
                c -= 2
                idx += 2
    print("".join(map(str,bnr)))
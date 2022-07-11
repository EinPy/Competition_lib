import sys
from collections import *
sys.setrecursionlimit(10**5)
itr = (line for line in sys.stdin.read().strip().split('\n'))
INP = lambda: next(itr)
def ni(): return int(INP())
def nl(): return [int(_) for _ in INP().split()]



def solve(n,a):
    pass


t = ni()
for case in range(t):
    e = INP()
    n, k = nl()
    st = nl()
    dat = {}
    for i in range(n):
        if st[i] not in dat:
            dat[st[i]] = [i]
        else:
            dat[st[i]].append(i)
    for _ in range(k):
        a, b = nl()
        if (a in dat and b in dat) and min(dat[a]) < max(dat[b]):
            print("YES")
        else:
            print("NO")

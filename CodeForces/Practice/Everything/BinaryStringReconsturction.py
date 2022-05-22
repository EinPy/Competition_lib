import sys
from collections import *
sys.setrecursionlimit(10**5)
itr = (line for line in sys.stdin.read().strip().split('\n'))
INP = lambda: next(itr)
def ni(): return int(INP())
def nl(): return [int(_) for _ in INP().split()]



def solve(s, x):
    n = len(s)
    w = ['1' for _ in range(n)]

    for i in range(n):
        if s[i] == '0':
            if i - x >= 0:
                w[i-x] = '0'
            if i + x < n:
                w[i+x] = '0'

    #print(w, s)

    for i in range(n):
        if s[i] == '1':
            #print(i, i-x, i+x)
            if (i-x >= 0 and w[i-x] == '1') or (i+x <n and w[i+x] =='1'):
                continue
            else:
                return -1

    return ''.join(w)

t = ni()
for case in range(t):
    s = INP()
    a = ni()
    print(solve(s, a))
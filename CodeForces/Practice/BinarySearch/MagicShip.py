import sys
from collections import *
sys.setrecursionlimit(10**5)
itr = (line for line in sys.stdin.read().strip().split('\n'))
INP = lambda: next(itr)
def ni(): return int(INP())
def nl(): return [int(_) for _ in INP().split()]



def ok(xd,yd, k, s, totCyc):
    cyc = k // len(s)
    left = k % len(s)
    moves = [cyc*totCyc[0],cyc*totCyc[1]]
    for i in range(left):
        moves[0] += s[i][0]
        moves[1] += s[i][1]
    #print(moves)

    #math part
    if k < abs(xd - moves[0]) + abs(yd-moves[1]):
        return False
    return True


def solve(n, s, x0, y0, xf, yf):
    xd = xf - x0
    yd = yf - y0
    s = list(s)
    for i in range(n):
        if s[i] == 'L':
            s[i] = (-1,0)
        if s[i] == 'R':
            s[i] = (1,0)
        if s[i] == 'U':
            s[i] = (0,1)
        if s[i] == 'D':
            s[i] = (0,-1)
    totCyc = [0,0]
    for d in s:
        totCyc[0] += d[0]
        totCyc[1] += d[1]
    n = len(s)

    l, r = 0, 2 * 10**20 + 1
    ans = -1
    #print(l, r)
    #print(xd, yd)
    #print(totCyc)
    while l <= r:
        mid = (l+r) // 2
        #print(mid)
        if ok(xd,yd, mid, s, totCyc):
            ans = mid
            r = mid -1
        else:
            l = mid + 1
    print(ans)

    


x0, y0 = nl()
xf, yf = nl()
n = ni()
s = INP()
solve(n, s, x0, y0, xf, yf)
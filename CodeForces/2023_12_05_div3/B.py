import sys
from collections import *
sys.setrecursionlimit(10**5)
itr = (line for line in sys.stdin.read().strip().split('\n'))
INP = lambda: next(itr)
def ni(): return int(INP())
def nl(): return [int(_) for _ in INP().split()]



def solve(a):
    ch =[]
    up = []
    for i in range(len(a)):
        if a[i] == 'b':
            if ch:
                ch.pop()
        elif a[i] == 'B':
            if up:
                up.pop()
        elif a[i].lower() == a[i]:
            ch.append((a[i], i))
        else:
            up.append((a[i],i))
    #print(ch)
    #print(up)
    ch.reverse()
    up.reverse()
    out = []
    while len(up) > 0 or len(ch) > 0:
        low, upp = 10000000000, 10000000000
        if ch:
            low = ch[-1][1]
        if up:
            upp = up[-1][1]
        #print(low, upp, up, ch)
        if low < upp:
            out.append(ch.pop()[0])
        else:
            out.append(up.pop()[0])
    if len(out) > 0:
        print("".join(out))
    else:
        print()
t = ni()
for case in range(t):
    a = INP()
    solve(a)
import sys
from collections import *
sys.setrecursionlimit(10**5)
itr = (line for line in sys.stdin.read().strip().split('\n'))
INP = lambda: next(itr)
def ni(): return int(INP())
def nl(): return [int(_) for _ in INP().split()]



def solve(a):
    if len(a) == 1:
        print(a * 2)
        return
    d = {}
    out = []
    for el in list(a):
        if el not in d:
            d[el] = 1
        else:
            d[el] += 1
    for k in d.keys():
        out.append(k * d[k])
    #print(d)
    rev = list(out[:])
    #print(out, rev)
    rev.reverse()
    #print(out, rev)
    out += rev
   # print(out)
    print(''.join(out))


t = ni()
for case in range(t):
    a = INP()
    solve(a)
import sys
from collections import *
sys.setrecursionlimit(10**5)
itr = (line for line in sys.stdin.read().strip().split('\n'))
INP = lambda: next(itr)
def ni(): return int(INP())
def nl(): return [int(_) for _ in INP().split()]

size, mod = nl()
week = 10080
best = 1e9

out = []
for _ in range(mod):
    poss = False
    m, price, cut, t, r = INP().split(",")
    price = int(price)
    cut = int(cut)
    t = int(t)
    r = int(r)
    out.append([price,m])
    
    tim = 10080 * t* cut
    
    if tim >= size * (t + r):
        poss = True
    if poss:
        if price < best:
            best = price
        
if best == 1e9:
    print("no such mower")
else:
    for i in out:
        if i[0] == best:
            print(i[1])
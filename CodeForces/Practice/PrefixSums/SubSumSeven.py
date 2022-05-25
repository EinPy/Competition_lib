import sys
from collections import *
sys.setrecursionlimit(10**5)
sys.stdin = open("div7.in")
sys.stdout = open("div7.out", "w")
itr = (line for line in sys.stdin.read().strip().split('\n'))
INP = lambda: next(itr)
def ni(): return int(INP())
def nl(): return [int(_) for _ in INP().split()]



def solve(n, a):
    pref = [0 for _ in range(n)]
    s = 0
    #print(a)
    for i, v in enumerate(a):
        s += v
        pref[i] = s % 7
    #print(pref)
    best = 0
    for i in range(7):
        #print(i)
        f, l = None, None
        for j in range(n):
            if pref[j] == i:
                if f == None:
                    f = j
                l = j
        #print(f, l)
        if f != None and l != None:
            best = max(l - f ,best)
    print(best)




t = ni()
a = []
for case in range(t):
    a.append(ni())
solve(t,a)
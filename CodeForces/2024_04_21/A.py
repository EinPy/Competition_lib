import sys
from collections import *
sys.setrecursionlimit(10**5)
itr = (line for line in sys.stdin.read().strip().split('\n'))
INP = lambda: next(itr)
def ni(): return int(INP())
def nl(): return [int(_) for _ in INP().split()]



n = ni()

for case in range(n):
    k, q = nl()
    arr = nl()
    players = nl()
    out = []
    for p in players:
        #Can literally simulate the entire thing?
        curp = p
        while curp >=  arr[0]:
            rem = 0
            for sub in arr:
                if sub <= curp:
                    rem += 1
            curp -= rem
        out.append(curp)
    print(" ".join(map(str,out)))
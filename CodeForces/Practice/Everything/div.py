import sys
from collections import *
sys.setrecursionlimit(10**5)
itr = (line for line in sys.stdin.read().strip().split('\n'))
INP = lambda: next(itr)
def ni(): return int(INP())
def nl(): return [int(_) for _ in INP().split()]


t = ni()
for case in range(t):
    INP()
    arr = []
    cols = [[] for _ in range(8)]
    for _ in range(8):
        l = INP()
        arr.append(l)
        for i in range(8):
            #print(l)
            #print(l[i])
            cols[i].append(l[i])
        
    fullR, fullB = False, False
    for r in range(8):
        if arr[r].count("R") == 8:
            fullR = True
        if arr[r].count("B") == 8:
            fullB = True
    for r in range(8):
        if cols[r].count("R") == 8:
            fullR = True
        if cols[r].count("B") == 8:
            fullB = True
    if fullR:
        print("R")
    else:
        print("B")
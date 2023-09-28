import sys
from collections import *
sys.setrecursionlimit(10**5)
itr = (line for line in sys.stdin.read().strip().split('\n'))
INP = lambda: next(itr)
def ni(): return int(INP())
def nl(): return [int(_) for _ in INP().split()]



t = ni()
arr = nl()
curD = 0
curScore = 0
wipes = 0
dirty = {}
for x in arr:
    dirty[x] = True
for i in range(1,366):
    
    curScore += curD
    #print(i, curScore, curD)
    if i in dirty:
        curD += 1
    if curScore + curD >= 20:
        wipes += 1
        curD = 0
        curScore = 0
if curD:
    wipes += 1
print(wipes)
import sys
from collections import *
sys.setrecursionlimit(10**5)
itr = (line for line in sys.stdin.read().strip().split('\n'))
INP = lambda: next(itr)
def ni(): return int(INP())
def nl(): return [int(_) for _ in INP().split()]



s = INP()
zoomL = len(s)
x, y = 0, 0
for p in range(len(s)-1,-1, -1):
    i = len(s)-1 - p
    step = 2 ** (p+1) / 2
    #print(i+1, step, s[i])
    if s[i] == '0':
        continue
    if s[i] == '1':
        x += step
    if s[i] == '2':
        y += step
    if s[i] == '3':
        x += step
        y += step
print(zoomL, int(x), int(y))
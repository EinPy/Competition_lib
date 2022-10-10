import sys
from collections import *
sys.setrecursionlimit(10**5)
itr = (line for line in sys.stdin.read().strip().split('\n'))
INP = lambda: next(itr)
def ni(): return int(INP())
def nl(): return [int(_) for _ in INP().split()]



a = ni()
b = ni()
clockwise = b - a
if clockwise < 0:
    clockwise = (360-a) + b
cc = a - b
if cc < 0:
    cc = a + (360-b)

if clockwise <= cc:
    print(clockwise)
else:
    if cc == 0:
        print(cc)
    else:
        print(f'-{cc}')
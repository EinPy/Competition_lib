import sys
from collections import *
sys.setrecursionlimit(10**5)
itr = (line for line in sys.stdin.read().strip().split('\n'))
INP = lambda: next(itr)
def ni(): return int(INP())
def nl(): return [int(_) for _ in INP().split()]



n = INP()
a = n.split("()")
if len(a[0])== len(a[1]):
    print("correct")
else:
    print("fix")

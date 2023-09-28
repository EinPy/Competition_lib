import sys
from collections import *
sys.setrecursionlimit(10**5)
itr = (line for line in sys.stdin.read().strip().split('\n'))
INP = lambda: next(itr)
def ni(): return int(INP())
def nl(): return [int(_) for _ in INP().split()]



n = ni()
s = list(INP().split())

fishy = False

for i in range(n):
    if s[i] != "mumble":
        if int(s[i]) != i + 1:
            fishy = True
            break

if not fishy:
    print("makes sense")
else:
    print("something is fishy")

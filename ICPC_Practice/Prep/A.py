import sys
from collections import *
sys.setrecursionlimit(10**5)
itr = (line for line in sys.stdin.read().strip().split('\n'))
INP = lambda: next(itr)
def ni(): return int(INP())
def nl(): return [int(_) for _ in INP().split()]



a = nl()
b = nl()
if sum(a) > sum(b):
    print("Gunnar")
elif sum(a) < sum(b):
    print("Emma")
else:
    print("Tie")
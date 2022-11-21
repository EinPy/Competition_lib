import sys
from collections import *
sys.setrecursionlimit(10**5)
itr = (line for line in sys.stdin.read().strip().split('\n'))
INP = lambda: next(itr)
def ni(): return int(INP())
def nl(): return [int(_) for _ in INP().split()]



n, x = nl()
arr = nl()
#all elements greater than x is divisible by x
#sum of all elements lower than x must be a multiple of x

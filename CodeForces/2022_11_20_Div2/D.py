import sys
from collections import *
sys.setrecursionlimit(10**5)
itr = (line for line in sys.stdin.read().strip().split('\n'))
INP = lambda: next(itr)
def ni(): return int(INP())
def nl(): return [int(_) for _ in INP().split()]



n, k = nl()
#binary jump f(x,y) = g(x) + g(y) - g(x, y)
#where g(x) is the number of ones in the binary
#representation of x
#find the number of pairs (a,b) such that
#f(a,b) = k, (a,b) and (b,a) are unique
#a and b < 2**(10**6) ( really fucking big)

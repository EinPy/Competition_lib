import sys
from collections import *
sys.setrecursionlimit(10**5)
itr = (line for line in sys.stdin.read().strip().split('\n'))
INP = lambda: next(itr)
def ni(): return int(INP())
def nl(): return [int(_) for _ in INP().split()]





t = ni()
pow = []
for i in range(11):
    pow.append(10**i)
pow.reverse()
#print(pow)
for case in range(t):
    n = ni()
    for num in pow:
        if num <= n:
            print(n - num)
            break
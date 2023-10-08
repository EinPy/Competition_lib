import sys
from collections import *
sys.setrecursionlimit(10**5)
itr = (line for line in sys.stdin.read().strip().split('\n'))
INP = lambda: next(itr)
def ni(): return int(INP())
def nl(): return [int(_) for _ in INP().split()]


dct = {"I" : 1, "V":5,'X':10,'L':50,'C':100,'D':500,'M':1000}

n = ni()
for _ in range(n):
    num = list(INP())
    curM = 0
    sum = 0
    for i in range(len(num)-1,-1,-1):
        if dct[num[i]] < curM:
            sum -= dct[num[i]]
        else:
            sum += dct[num[i]]
            curM = dct[num[i]]
    print(sum)
import sys
from collections import *
sys.setrecursionlimit(10**5)
itr = (line for line in sys.stdin.read().strip().split('\n'))
INP = lambda: next(itr)
def ni(): return int(INP())
def nl(): return [int(_) for _ in INP().split()]

import math

f = INP()
s = INP()

fG, sG, u = 0, 0, 0
n = len(f)

for i in range(n):
    if f[i] == '+':
        fG += 1
    if f[i] == '-':
        fG -= 1
    if s[i] == '+':
        sG += 1
    if s[i] == '-':
        sG -= 1
    if s[i] == '?':
        u += 1

diff = abs(fG - sG)
#print(sG, fG, diff)
if diff > u or (diff + u) %2 != 0:
    print(0)
else:
    movesInDir = diff + (u - diff) // 2
    prob = math.comb(u, movesInDir) / 2**u
    print(prob)

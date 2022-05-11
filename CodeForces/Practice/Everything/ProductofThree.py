import sys
from collections import *
sys.setrecursionlimit(10**5)
itr = (line for line in sys.stdin.read().strip().split('\n'))
INP = lambda: next(itr)
def ni(): return int(INP())
def nl(): return [int(_) for _ in INP().split()]

import math

t = ni()
for case in range(t):
    n = ni()
    a, b = 0, 0
    for i in range(2, int(math.sqrt(n)+1)):
        if n % i == 0:
            a = i
            n = n // i
            break
    for i in range(2, int(math.sqrt(n)+1)):
        if i != a and n % i == 0:
            b = i
            n = n // i
            break

    #print(a, b, n)
    if a and b:
        if n != a and n != b:
            print("YES")
            print(f"{a} {b} {n}")
        else:
            print("NO")
    else:
        print("NO")
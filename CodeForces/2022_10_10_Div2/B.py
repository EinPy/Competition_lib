import sys
from collections import *
sys.setrecursionlimit(10**5)
itr = (line for line in sys.stdin.read().strip().split('\n'))
INP = lambda: next(itr)
def ni(): return int(INP())
def nl(): return [int(_) for _ in INP().split()]


def gcd(a, b):
	if a == 0:
		return b
	return gcd(b%a, a)
import math

#if a greater number follows that is a multiple of the previous number
def solve(n,a):
    if n == 1:
        print("YES")
        return
    for i in range(n-2):
        #previous number is divisible by three.
        #nån siffra ska va delbar på 4 och två, och 
        if gcd(a[i],a[i+1]) == a[i+1] and not (a[i] == a[i+1] and [a[i+1] == a[i+2]]):
            print("NO")
            return
    print("YES")



t = ni()
for case in range(t):
    n = ni()
    a = nl()
    solve(n,a)
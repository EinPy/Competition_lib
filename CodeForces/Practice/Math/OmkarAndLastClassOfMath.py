import sys
from collections import *
sys.setrecursionlimit(10**5)
itr = (line for line in sys.stdin.read().strip().split('\n'))
INP = lambda: next(itr)
def ni(): return int(INP())
def nl(): return [int(_) for _ in INP().split()]

import math

def gcd(a, b):
	if a == 0:
		return b
	return gcd(b%a, a)

def lcm(a, b):
	product = a*b
	#highest common factor == greatest common divisor
	hcf = gcd(a, b)
	return product // hcf

t = ni()
for case in range(t):
    n = ni()

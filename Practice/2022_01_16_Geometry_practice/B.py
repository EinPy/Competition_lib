def setupInputOutputSublime():
	import sys
	import os

	if os.name == 'nt':
		sys.stdout = open("C:\\Temp\\output.txt", mode = 'w')
		sys.stdin = open("C:\\Temp\\input.txt", mode = 'r')
setupInputOutputSublime()


from math import sqrt
from collections import Counter
from fractions import Fraction



def gcd(a, b):
	if a == 0:
		return b
	return gcd(b%a, a)

def lcm(a, b):
	product = a*b
	#highest common factor == greatest common divisor
	hcf = gcd(a, b)
	return product // hcf

def allDivisors(n):
	#O(sqrt(n))
	div2 = set()
	for i in range(1, int(sqrt(n))+1): #range [1, root(n)]
		if n%i == 0:
			div2.add(i)
			div2.add(n//i)
	return div2

def primeTest(n):
	#T.C = O(root(n))
	if n == 0 or n == 1: #O(1)
		return False
	if n == 2 or n == 3: #O(1)
		return True
	if n%2 == 0 or n%3 == 0: #O(1)
		return False
	for i in range(5,int(sqrt(n))+1): # [1, root (n)]
		if n%i == 0 or n%(i+2) == 0:
			return False
	return True

def generate_primes(n):
	primes = [True]*(n+1)
	primes[0], primes[1] = False, False
	for p in range(2, int(sqrt(n)) + 1):
		if primes[p]:
			for i in range(p*p, n+1, p):
				primes[i] = False

	out = []
	for i, n in enumerate(primes):
			if n:
				out.append(i)
	return out

#start here



# Converts two points to a line (a, b, c), 
# ax + by + c = 0
# if p == q, a = b = c = 0
def pts2line(p, q):
	a = -q[1] + p[1]
	b = q[0] - p[0]
	c = p[0]*q[1] - p[1]*q[0]
	return (a, b, c)


def normalize(a,b,c):
	if a == 0:
		return 0, 1, Fraction(c, b)
	if a < 0:
		a, b, c = -a, -b, -c
	factor = gcd(a, abs(b))
	a, b, c = a//factor, b//factor, Fraction(c, factor)
	return a, b, c


def crossZ(p, q):
	return p[0]*q[1] - q[0]*p[1]

def vec(p, q):
	return q[0] - p[0], q[1] - p[1]

def is_multiple(x,y):
    if x!=0 and (y%x)==0:
    	return True
    elif x!= 0 and (x%y) == 0:
    	return True


#colinear points
#W, N = (list(map(int,input().split())))
#print(W, N)

#test cases 
while True:
	T = int(input())
	if T != 0:
		points = []
		for i in range(T):
			x, y = (list(map(int,input().split())))
			points.append((x,y))

		points.sort()
		M = 1
		for i, p1 in enumerate(points):
			lines = Counter()
			for j, p2 in enumerate(points):
				if i != j:
					lines[normalize(*pts2line(p1, p2))] += 1
			if lines.values():
				M = max(M, max(lines.values()) + 1)

		print(M)
	else:
		break


	









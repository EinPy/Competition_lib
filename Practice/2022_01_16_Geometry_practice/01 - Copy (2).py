from math import sqrt

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
def setupInputOutputSublime():
	import sys
	sys.stdout = open("C:\\Temp\\output.txt", mode = 'w')
	sys.stdin = open("C:\\Temp\\input.txt", mode = 'r')
setupInputOutputSublime()

def pts2line():
	pass

def normalize(a,b,c):
	pass

def crossZ(p, q):
	return p[0]*q[1] - q[0]*p[1]

def vec(p, q):
	return q[0] - p[0], q[1] - p[1]



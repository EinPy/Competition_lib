import sys

def setupInputOutputSublime():
	import os

	if os.name == 'nt':
		sys.stdout = open("C:\\Temp\\output.txt", mode = 'w')
		sys.stdin = open("C:\\Temp\\input.txt", mode = 'r')
setupInputOutputSublime()
from math import sqrt

itr = (line for line in sys.stdin.read().strip().split('\n'))
input = lambda: next(itr)

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


def pts2line():
	pass

def normalize(a,b,c):
	pass

def crossZ(p, q):
	return p[0]*q[1] - q[0]*p[1]

def vec(p, q):
	return q[0] - p[0], q[1] - p[1]


def convexHull(points): #input in typles with coordinates (x,y)
	points.sort() #sort by x
	def getHull(points):
		UPP = [] # upper part of Hull
		#adding the two leftmost points
		UPP.append(points[0])
		UPP.append(points[1])
		for p in points[2:]:
			while len(UPP) > 1: 
				v1 = vec(UPP[-1], UPP[-2])
				v2 = vec(UPP[-1], p)
				if crossZ(v1, v2) > 0:
					break 
				UPP.pop()
			UPP.append(p)
		return UPP
	UPP = getHull(points)
	LOW = getHull(points[::-1])

	return UPP[1:] + LOW[1:]

lines = []
while True:
	T = int(input())
	if T != 0:
		arr = []
		for i in range(T):
			x, y = (list(map(int,input().split())))
			arr.append((x,y))
		arr = list(set(arr))
		if len(arr) >= 2:
			out = convexHull(arr)[::-1]
			lines.append(f"{len(out)}")
			for x, y in out:
				lines.append(f"{x} {y}")
		else:
			lines.append("1")
			lines.append(f"{arr[0][0]} {arr[0][1]}")
	else:
		break
print("\n".join(lines))
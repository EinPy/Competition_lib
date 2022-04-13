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


#code starrts here:
#https://codeforces.com/contest/492/problem/B

n, l = list(map(int,input().split()))
lnt = [0] + list(map(int,input().split()))
lnt.sort()
lnt.append(l)
greatest_dist = 0

for i in range(n+1):
	if i == 0:
		greatest_dist = max((lnt[i+1] - lnt[i]) * 2, greatest_dist)
	elif i == n:
		greatest_dist = max((lnt[i+1] - lnt[i]) * 2, greatest_dist)
	else:
		greatest_dist = max(lnt[i+1] - lnt[i], greatest_dist)

print(greatest_dist/2)
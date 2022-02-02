import sys


def setupInputOutputSublime():
	import os

	if os.name == 'nt':
		sys.stdout = open("C:\\Temp\\output.txt", mode = 'w')
		sys.stdin = open("C:\\Temp\\input.txt", mode = 'r')
setupInputOutputSublime()
from math import sqrt
#https://codeforces.com/problemset/problem/580/B
itr = (line for line in sys.stdin.read().strip().split('\n'))
input = lambda: next(itr)

n, d = list(map(int,input().split()))
f = []
for i in range(n):
	m, ff = list(map(int,input().split()))
	f.append((m, ff))
f.sort()


best = 0
for l in range(n):
	r = n-1
	while f[r][0] - f[l][0] >= d:
		mid = (r + l)//2
		if f[mid][0] - f[l][0] >= d:
			r = mid - 1
			continue
		else:
			while f[mid][0] - f[l][0] < d:
				mid = (mid+ 1 + r) // 2
			r = mid-1
	tot = 0
	for i in range(l, r+1):
		tot += f[i][1]
	best = max(best, tot)

print(best)

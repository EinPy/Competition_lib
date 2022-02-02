import sys


def setupInputOutputSublime():
	import os

	if os.name == 'nt':
		sys.stdout = open("C:\\Temp\\output.txt", mode = 'w')
		sys.stdin = open("C:\\Temp\\input.txt", mode = 'r')
#setupInputOutputSublime()


#https://codeforces.com/problemset/problem/580/B
itr = (line for line in sys.stdin.read().strip().split('\n'))
input = lambda: next(itr)

n, d = list(map(int,input().split()))
f = []
for i in range(n):
	m, ff = list(map(int,input().split()))
	f.append((m, ff))
f.sort()
#print(f)
#not true
best = 0
curTot = f[0][1]
best = curTot
#sliding window approach
l, r = 0, 1
if len(f) == 1:
	best = f[0][1]
	print(best)
else:
	while True:
		if f[r][0] -f[l][0] >= d:
			best = max(curTot, best)
			l+=1
			if l == r:
				curTot += f[l][1]
			curTot -= f[l-1][1]
		else:
			if l != r:
				curTot += f[r][1]
			r+=1

		if r == n:
			best = max(best, curTot)
			break
	print(best)
	
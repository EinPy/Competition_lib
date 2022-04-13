import sys


def setupInputOutputSublime():
	import os

	if os.name == 'nt':
		sys.stdout = open("C:\\Temp\\output.txt", mode = 'w')
		sys.stdin = open("C:\\Temp\\input.txt", mode = 'r')
#setupInputOutputSublime()


#https://codeforces.com/contest/489/problem/B?csrf_token=2ac8a9589b0d8691a16b067b699a06e7
itr = (line for line in sys.stdin.read().strip().split('\n'))
input = lambda: next(itr)

n = int(input())
boy = list(map(int,input().split()))
m = int(input())
girl = list(map(int,input().split()))
boy.sort()
girl.sort()

#print(boy)
#print(girl)
pb, pg = 0, 0
pairs = 0
def comp(a,b):
	if abs(a-b) <= 1 : return True
bTaken = False
gTaken = False
while True:
#	print(pb, pg)
	if comp(boy[pb], girl[pg]):
		pairs += 1
		if pb + 1 < n:
			pb +=1
		else:
			break
		if pg + 1 < m:
			pg +=1
		else:
			break
	else:
		if pb + 1 < n and boy[pb] < girl[pg]:
			pb += 1
		elif pg + 1 < m and girl[pg] < boy[pb]:
			pg += 1
		else:
			break

print(pairs) 

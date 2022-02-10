import sys

def setupInputOutputSublime():
    import os

    if os.name == 'nt':
        sys.stdout = open("D:\\Temp\\output.txt", mode = 'w')
        sys.stdin = open("D:\\Temp\\input.txt", mode = 'r')
#setupInputOutputSublime()
from math import sqrt


itr = (line for line in sys.stdin.read().strip().split('\n'))
input = lambda: next(itr)

#https://codeforces.com/problemset/problem/327/A
n = int(input())
a = list(map(int,input().split()))
best = 0
for l in range(n):
    for r in range(l, n):
        p1 = l
        tmp = a[:]
        while p1 <=r:
            if tmp[p1] == 0:
                tmp[p1] = 1
            else:
                tmp[p1] = 0
            p1 += 1
        best = max(tmp.count(1), best)
print(best)







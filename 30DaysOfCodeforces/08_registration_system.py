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

#solution to https://codeforces.com/problemset/problem/466/A
#code starts here
    
n = int(input())
data = {}
for i in range(n):
    newN = str(input())
    if newN not in data:
        data[newN] = 0
        print("OK")
    else:
        data[newN] += 1
        newN += str(data[newN])
        print(newN)
        data[newN] = 0

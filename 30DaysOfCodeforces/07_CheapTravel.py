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
    


n,m,a,b = list(map(int,input().split()))

money= 0 
if b/m < a:
    ms = n//m
    money += ms*b + (n-ms*m) * a
else:
    money = n*a
print(money)
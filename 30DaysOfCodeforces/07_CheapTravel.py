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

#solution to https://codeforces.com/problemset/problem/4/C
#code starts here
    


n,m,a,b = list(map(int,input().split()))

money= 0 
if b/m < ac56r:
    if m <= n:
        ms = n//m
        if b > a:
            money += ms*b + (n-ms*m) * a
        else:
            if ms*m != n:
                money += ms*b + b
            else:
                money = ms*b
    else:
        if b < n*a:
            money = b
        else:
            money = n*a
else:
    money = n*a
print(money)
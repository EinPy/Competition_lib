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


def solve(c, o):
    cT = min(c)
    oT = min(o)
    ops = 0
    for i in range(len(c)):
        common = min(c[i] - cT, o[i] - oT)
#        print(common)
        ops += common
        ops += c[i] - common - cT
        ops += o[i] - common - oT
    return ops



T = int(input())
for i in range(T):
    n = int(input())
    c = list(map(int,input().split()))
    o = list(map(int,input().split()))
    print(solve(c,o))
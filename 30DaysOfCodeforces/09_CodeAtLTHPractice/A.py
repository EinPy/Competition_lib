import sys

def setupInputOutputSublime():
    import os

    if os.name == 'nt':
        sys.stdout = open("D:\\Temp\\output.txt", mode = 'w')
        sys.stdin = open("D:\\Temp\\input.txt", mode = 'r')
setupInputOutputSublime()
from math import sqrt

itr = (line for line in sys.stdin.read().strip().split('\n'))
input = lambda: next(itr)

#code starts here
def solve():
    h, w, n = list(map(int,input().split()))

    bricks = list(map(int,input().split()))
    cur = 0
    curH = 0
    can = True
    i = 0
    while curH <= h and i < len(bricks):
        cur += bricks[i]
        i+=1
        if cur == w:
            if curH != h:
                curH+= 1
                cur = 0
            if curH = h
        else:
            if cur > w:
                break
    if curH == h:
        print("YES")
    else:
        print("NO")


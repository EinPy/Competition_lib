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

#print("tests") 



def solve(a):
    if len(a) == 1:
        return True
    if min(a) == max(a):
        return True
    a.sort()
    while len(a) > 1:
        if len(a) >= 3:
            p0, p1, p2 = a[0], a[1], a[2]
            if abs(p1 - p0) <= 1:
                a.pop(0)
            else:
                if abs(p2-p1) <= 0:
                    a.pop(1)
                else:
                    return False
        if len(a) == 2:
            p0, p1 = a[0], a[1]
            if abs(p1 - p0) <= 1:
                return True
            else:
                return False

    return True


T = int(input())
for i in range(T):
    n = int(input())
    a = list(map(int,input().split()))
#    print(a)
    if solve(a):
        print("YES")
    else:
        print("NO")

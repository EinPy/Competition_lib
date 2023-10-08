import sys
from collections import *
sys.setrecursionlimit(10**5)



mi = 0
ma = 2

def q(x):
    print("buf["+str(x)+"]",flush=True)
    return int(input())!=0

while q(ma):
    ma*=2

mi = ma//2
mid = (mi+ma)//2

while ma-mi > 1:
    mid = (mi+ma)//2
    if q(mid):
        mi = mid
    else:
        ma = mid

print("strlen(buf) = "+str(ma),flush=True)
exit()
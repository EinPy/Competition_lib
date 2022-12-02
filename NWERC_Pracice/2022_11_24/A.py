import sys
from collections import *
sys.setrecursionlimit(10**5)
itr = (line for line in sys.stdin.read().strip().split('\n'))
INP = lambda: next(itr)
def ni(): return float(INP())
def nl(): return [float(_) for _ in INP().split()]


bounds = []
c=0
for _ in range(int(INP())):
    a,b = nl()
    c+=a
    bounds.append((c,b/100))
bounds.append((10**16,ni()/100))

#print(bounds)
def nextt(curr):
    i = 0
    while(bounds[i][0]<=curr):
        i+=1
    return((bounds[i][0]-curr,bounds[i][1]))

for _ in range(int(INP())):
    #dist,tax = (0,0.5)
    give = 0
    curr,left = nl()
    dist,tax= nextt(curr)
    
    #print("case",curr,left)
    
    while left>dist*(1-tax):
        give+=dist
        curr+=dist
        left-=dist*(1-tax)
        #print("curr:",curr,"dist:",dist)
        dist,tax=nextt(curr)
        #print("ret",dist,tax)
    
    give+=left/(1-tax)
    
    print(give)



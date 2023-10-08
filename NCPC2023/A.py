import sys
from collections import *
sys.setrecursionlimit(10**5)



n,k = map(int,input().split())

def solve(n,k):
    if n<=k:
        return 0
    
    iters = 0
    count = 0
    size = 1
    
    while n>k*size:

        size=size*k+1
        count=count*k+1
        iters +=1
        
        if iters == k:
            return count+n-size
    #print(size,count)
    ans = count*(n//size) + solve(n%size,k)
    
    #print("hej",n,k,ans)
    return ans

print(solve(n,k))
    
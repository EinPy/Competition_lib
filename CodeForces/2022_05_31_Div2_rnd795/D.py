import sys
from collections import *
sys.setrecursionlimit(10**5)
itr = (line for line in sys.stdin.read().strip().split('\n'))
INP = lambda: next(itr)
def ni(): return int(INP())
def nl(): return [int(_) for _ in INP().split()]

  
def maxSubArraySum(arr,size):

    max_till_now = arr[0]
    max_ending = 0

    for i in range(0, size):
        max_ending = max_ending + arr[i]
        if max_ending < 0:
            max_ending = 0
        
        
        elif (max_till_now < max_ending):
            max_till_now = max_ending
            
    return max_till_now
  
  

def solve(n,a):
    sumPos = 0
    sumNeg = 0
    curMax = 0
    for i in range(n-1):
        curMax = max(curMax, a[i])
        if a[i] >0:
            sumPos += a[i]
        if a[i] < 0:
            sumNeg += a[i]
        if a[i] > 0 and a[i+1] > 0:
            return "NO"
        
    if curMax < sumPos + sumNeg:
        #print("here")
        return "NO"
        
    curMax = 0
    curSum = 0
    for i in range(n):
        curSum += a[i]
        curMax = max(curMax, a[i])
        if curSum > curMax:
            return "NO"
        if a[i] > 0 and a[i] < curMax:
            curSum = 0
            curMax = 0
        
        
    
    
    return "YES"


t = ni()
for case in range(t):
    n = ni()
    a = nl()
    print(solve(n,a))
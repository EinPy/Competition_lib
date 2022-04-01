import sys
sys.setrecursionlimit(10**5)
itr = (line for line in sys.stdin.read().strip().split('\n'))
input = lambda: next(itr)

#code
import re

def score(s,x, y):
    cost = 0
    for i in range(len(s)-1):
        if s[i] == "C" and s[i+1] == "J":
            cost += x
        if s[i] == "J" and s[i+1] == "C":  
            cost += y
    return cost

def rec(s, x, y, mem = {}):
    if "?" not in s:
        return 
    
    indices = [i.start() for i in re.finditer("?", s)]
    for i in indices:
        
        


def solve(s):
    print(s)
    iC = score(s[2],int(s[0]), int(s[1]))
    print(iC)
    rec(s[2],int(s[0]), int(s[1]))




T = int(input())
for case in range(1,T+1):
    arr = input().split()
    c = solve(arr)
    print(f"Case #{case}: {c}")
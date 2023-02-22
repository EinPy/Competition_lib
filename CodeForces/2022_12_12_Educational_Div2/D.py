import sys
from collections import *
sys.setrecursionlimit(10**5)
itr = (line for line in sys.stdin.read().strip().split('\n'))
INP = lambda: next(itr)
def ni(): return int(INP())
def nl(): return [int(_) for _ in INP().split()]

def gcd(a, b):
    if b == 0:
        return a
    else:
        return gcd(b, a % b)

def longest_lucky_chain(x, y):
    if gcd(x, y) != 1:
        return 0
    else:
        k = 0
        if x == y+1 or y == x+1:
            return -1
        while gcd(x + k, y + k) == 1:
            if k >= 200:
                return -1
            k += 1
        return k
    
    
n = ni()
pairs  = []
for l in range(n):
    pairs.append(nl())
    

# For each pair, calculate the length of the longest lucky chain induced by the pair
for pair in pairs:
    # Calculate the length of the longest lucky chain induced by the pair
    length = longest_lucky_chain(pair[0], pair[1])
    # If the length of the chain is greater than 0, print the length of the chain
    print(length)

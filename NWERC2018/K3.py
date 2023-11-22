import sys
from collections import *
sys.setrecursionlimit(10**5)
itr = (line for line in sys.stdin.read().strip().split('\n'))
INP = lambda: next(itr)
def ni(): return int(INP())
def nl(): return [int(_) for _ in INP().split()]



N, M = nl()
end = INP()
b = INP()

#check backwards
key = ["0"] * (N + M)
for i in range(N):
    key[i+ M] = end[i]
    
#print(key)
for i in range(-1, -M-1, -1):
    #b[-1] should be comb of k[-1] and k[-1 ]
    #print(i)
    for j in range(26):
        if ord(b[i]) - 97 == (ord(key[i]) - 97 + j) % 26:
            key[i - N] = chr(j + 97)
#print(key)
print("".join(key[N:]))
        
import sys
from collections import *
sys.setrecursionlimit(10**5)
itr = (line for line in sys.stdin.read().strip().split('\n'))
INP = lambda: next(itr)
def ni(): return int(INP())
def nl(): return [int(_) for _ in INP().split()]



N, M = nl()
#keyword and number of letters
#m is length of text
n = INP()
m = INP()

out = ["a"] * (N + M)
out[-1] = n[-1]
for i in range(-1, -M, -1):
    print(i)
    if abs(i) <= N:
        print("yes")
        for j in range(26):
            if (ord(n[i]) - 97 + j) % 26 == ord(m[i]) - 97:
                out[i - N] = chr(j + 97)
                break
        
    else:
        for j in range(26):
            if (ord(out[i])- 97 + j) % 26 == ord(m[i]) - 97:
                out[i - N] = chr(j + 97)
                break
        
print(out)
print(chr((ord('r') - 97 + ord('d') - 97)))
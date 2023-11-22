import sys
from collections import *
sys.setrecursionlimit(10**5)
itr = (line for line in sys.stdin.read().strip().split('\n'))
INP = lambda: next(itr)
def ni(): return int(INP())
def nl(): return [int(_) for _ in INP().split()]



n, m = nl()
#keyword and number of letters
#m is length of text
k = INP()
m = INP()

print(ord('a')-97, ord('z')- 97, chr(2 + 97))

T = m[-n:]
print(T)

key = []
for i in range(n):
    for j in range(26):
        print(k[i], chr((ord(k[i]) - 97 + j) % 26+ 97) )
        if chr((ord(k[i]) - 97 + j) % 26 + 97) == T[i]:
            key.append(chr(j + 97))
            break
        
        
#backwards apporach
#fill length of key
mr = m[-1::-1]
print(mr)
total = ["0"] * (n + len(m))
for i in range()

            
print(key, (chr((ord('r') - 97 + ord('o') - 97) % 26 + 97)))
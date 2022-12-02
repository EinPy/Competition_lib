import sys
from collections import *
sys.setrecursionlimit(10**5)
itr = (line for line in sys.stdin.read().strip().split('\n'))
INP = lambda: next(itr)
def ni(): return int(INP())
def nl(): return [int(_) for _ in INP().split()]



w = INP()
siz = len(w)
n = ni()
rhymes = []
for l in range(n):
    words = INP().split()
    for let in words:
        if len(let) <= len(w):
            if w[siz - len(let):] == let:
                #print(let)
                rhymes += words
                break
    
    #print(words)
    #print(rhymes)
    
#print(rhymes)
d = {}
for word in rhymes:
    d[word] = True
n = ni()
for l in range(n):
    words = INP().split()
    word = words[-1]
    found = False
    for i in range(len(word)):
        #print(word[i:])
        if word[i:] in d:
            print("YES")
            found = True
            break
    if not found:
        print("NO")
    
    

from string import ascii_lowercase, ascii_uppercase
import sys
from collections import *
sys.setrecursionlimit(10**5)
itr = (line for line in sys.stdin.read().strip().split('\n'))
INP = lambda: next(itr)
def ni(): return int(INP())
def nl(): return [int(_) for _ in INP().split()]


n, m = nl()
s = ord('z') -ord('a') + 1

one = [False for _ in range(s)]
two = [[False for _ in range(s)] for _ in range(s)]
three = [[[-1 for _ in range(s)] for _ in range(s)] for _ in range(s)] 

times = 0
words = [''] * n
for i in range(n):
    for j in range(s):
        one[j] = False
        for k in range(s):
            two[j][k] = False
            
    word = INP()
    for j in range(len(word)):
        for k in range(s):
            for l in range(s):
                if two[k][l] and three[k][l][ord(word[j]) - ord('a')] == -1:
                    three[k][l][ord(word[j]) - ord('a')] = i
                    
            two[k][ord(word[j]) - ord('a')] |= one[k]
                      
        one[ord(word[j]) - ord('a')] = True
        
    words[i] = word

out = []
for i in range(m):
    plate = list(INP())
    a = three[ord(plate[0]) - ord('A')][ord(plate[1]) - ord('A')][ord(plate[2]) - ord('A')]
    if a == -1:
        out.append("No valid word")
    else:
        out.append(words[a])
        
print('\n'.join(out))
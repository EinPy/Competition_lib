import sys
from collections import *
sys.setrecursionlimit(10**5)
itr = (line for line in sys.stdin.read().strip().split('\n'))
INP = lambda: next(itr)
def ni(): return int(INP())
def nl(): return [int(_) for _ in INP().split()]



L = ni()
S = list(INP())[1:]
print(len(S), S)
fg = ni()
g_score = 0
for i in range(fg-1, fg + 3):
    if S[i] == 'b':
        g_score += 1
        S[i] = '.'
        
#get ranges:
sequences = []
four_plus = []
fours = []
threes = []
twos = []
one = []

isSeq = False
beg = -1
for i in range(len(S)):
    if isSeq:
        if S[i] == 'b':
            continue
        else:
            sequences.append([beg, i-1])
            isSeq = False
            size = i-1  - beg +1
            if i == 1:
                one.append(beg)
            if i == 2:
                twos.append(beg)
            if i == 3:
                threes.append(beg)
            if i == 4:
                fours.append(beg)
            if i > 4:
                four_plus.apppend(beg)
    else:
        if S[i] == 'b':
            beg = i
            isSeq = True
        else:
            continue
if isSeq:
    sequences.append([beg, L-1])
        

print(S)
print(sequences)
    
import sys
from collections import *
sys.setrecursionlimit(10**5)
itr = (line for line in sys.stdin.read().strip().split('\n'))
INP = lambda: next(itr)
def ni(): return int(INP())
def nl(): return [int(_) for _ in INP().split()]



n = ni()
sent = list(INP().split())
m = ni()
dict = {}
for _ in range(m):
    dut, eng, state = INP().split()
    if dut not in dict:
        dict[dut] = [[],[]]
    if state[0] == "c":
        dict[dut][1].append(eng)
    else:
        dict[dut][0].append(eng)
        
corr = 1
tot = 1 #there will always exist a translation?

for word in sent:
    corr *= len(dict[word][1]) #if a word has no correct corr = 0
    tot *= (len(dict[word][0]) + len(dict[word][1]))


if tot == 1: #only one translations
    out = []
    for word in sent:
        if len(dict[word][1]) != 0:
            out.append(dict[word][1][0])
        if len(dict[word][0]) != 0:
            out.append(dict[word][0][0])
        
    print(' '.join(list(map(str, out))))
    if corr == 1: print("correct")
    else: print("incorrect")
    
else:
    print(corr, "correct")
    print(tot - corr, "incorrect")
    

import sys
from collections import *
sys.setrecursionlimit(10**5)
itr = (line for line in sys.stdin.read().strip().split('\n'))
INP = lambda: next(itr)
def ni(): return int(INP())
def nl(): return [int(_) for _ in INP().split()]



def solve(dies, i):
    die = dies[i]
    
    for l in range(3):
        if i != l:
            wins = 0
            x = 36
            for j in range(6):
                for k in range(6):
                    if die[j] > dies[l][k]:
                        wins += 1
                    elif die[j] == dies[l][k]:
                        x -= 1
            if x == 0:
                return False  
            if wins / x < 0.5:
                return False
            
    return True     

dies = []

for _ in range(3):
    dies.append(nl())

best_dies = []

for i in range(3):
    if solve(dies, i):
        best_dies.append(i + 1)

if len(best_dies) == 0:
    print('No dice')
else:
    print(min(best_dies))
    
from string import ascii_lowercase, ascii_uppercase
import sys
from collections import *
sys.setrecursionlimit(10**5)
itr = (line for line in sys.stdin.read().strip().split('\n'))
INP = lambda: next(itr)
def ni(): return int(INP())
def nl(): return [int(_) for _ in INP().split()]

s = ord('z') - ord('a') + 1
words = [['' for _ in range(102)] for _ in range(102)]
first = [[-1 for _ in range(5000)] for _ in range(s)]
last = [[-1 for _ in range(5000)] for _ in range(s)]
cumsum = [[[0 for _ in range(102)]  for _ in range(s)] for _ in range(5000)]

n, m = nl()
for i in range(n):
    words[i] == INP()
    for k in range(words[i][0]):
        last[i]

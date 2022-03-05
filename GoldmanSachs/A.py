import string
import sys
itr = (line for line in sys.stdin.read().strip().split('\n'))
input = lambda: next(itr)

N = int(input())
words = list(map(str,input().split()))
buzzes = {"he" : True, "she" : True, "him" : True, "her" : True}
#print(words)
out = 0
for w in words:
    if w.lower() in buzzes:
        out += 1
        
print(out)

import sys
from collections import *
sys.setrecursionlimit(10**5)
itr = (line for line in sys.stdin.read().strip().split('\n'))
INP = lambda: next(itr)
def ni(): return int(INP())
def nl(): return [int(_) for _ in INP().split()]



s, b = INP().split()
arr = list("!\"#$%&'()*+,-./")
#-32
a = 0
for l in list(s):
    a += ord(l)-32
a += 32

#print(ord('*')-32, ord('h'), chr(33), chr(-ord('*')+ord('h')), chr(ord('\'')-ord('*')+ord('h')))
out = []
while True:
    try:
        line = INP().split()
        for w in line:
            #print(w)
            if w == '>':
                out.append('.')
            elif w == '<':
                out.append(',')
            elif w == '0':
                out.append(" ")
            else:
                t = 0
                for l in list(w):
                    t += ord(l)-32
                t += 32
                o = (t + ord(b) - a)
                if o < ord('a'):
                    o += 26
                if o > ord('z'):
                    o -= 26
                out.append(chr(o))
        out.append('\n')
    except:
        break


        
    #print(out)
out = ''.join(out)
print(out[:-1])
        
        
        

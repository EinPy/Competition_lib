import sys
from collections import *
sys.setrecursionlimit(10**5)



L = int(input())
S = list(input().replace('.',"0").replace('b',"1"))
S = list(map(int,S))
        

take = [0] * L
for i in range(len(S)-3):
    take[i] = S[i]*(S[i] + S[i+1] + S[i+2] + S[i+3])
    #print(i)

take[-3] = S[-3]*(S[-3] + S[-2] + S[-1])
take[-2] = S[-2]*(S[-2] + S[-1])
take[-1] = S[-1]


dct = {i:defaultdict(set) for i in range(1,5)}
diffs = [0]*len(S)
tot = [0,0,0,0]

for i in range(len(S)-3):
    if take[i]==0:
        continue
    
    vals = take[i:i+4]
    
    tup = tuple(vals.count(4-i)%2 for i in range(4))
    dct[take[i]][tup].add(i)
    for i in range(4):
        tot[i] += vals.count(4-i)

for i in range(len(S)-3,L):
    if take[i]==0:
        continue
    
    vals = take[i:]
    
    tup = tuple(vals.count(4-i)%2 for i in range(4))
    dct[take[i]][tup].add(i)
    for i in range(4):
        tot[i] += vals.count(4-i)

def update(i):    
    tups = []
    #print("i",i)
    
    for j in range(max(0,i-3),i):
        vals = take[j:j+4]
        if take[j]!=0:     
            tups.append((tuple(vals.count(4-i)%2 for i in range(4)),j,take[j]))
        
    for j in range(i,min(i+4,L)):
        S[j] = 0
    
   
    
    for t,j,ta in tups:
        #print(t,j,ta)
        if j in dct[ta][t]:
            dct[ta][t].remove(j)
        vals = take[j:j+4]
        
        dct[take[j]][tuple(vals.count(4-i)%2 for i in range(4))].add(j)
    
    for j in range(min(4, L-j)):
        tot[take[i+j]] -=1
        
    for j in range(max(0,i-3),i):
        vals = S[j:min(j+4,L)]
        take[j] = S[i]*sum(vals)
    
    
    for k,d in dct.items():
        for s in d.keys():
            for j in range(i,i+4):
                if j in d[s]:
                    d[s].remove(j)
    
    if tot == [0,0,0,0]:
        exit()
    
    print("take:",take,"\n dct",dct,"\n tot",tot)

def match(t1,t2):
    return 8*int(t1[0]==t2[0]) + 4*int(t1[1]==t2[1])+ 2*int(t1[2]==t2[2]) + int(t1[3]==t2[3])




while True:
    i = int(input())-1
    while S[i]==0:
        i+=1
    
    taken = take[i]
    
    update(i)
    
    tuples = [(0,0,0,0),(0,0,0,1),(0,0,1,0),(0,0,1,1),(0,1,0,0),(0,1,0,1),(0,1,1,0),(0,1,1,1),(1,0,0,0),(1,0,0,1),(1,0,1,0),(1,0,1,1),(1,1,0,0),(1,1,0,1),(1,1,1,0),(1,1,1,1)]
    j = ""
    d = dct[taken]
    tot_cop = [t%2 for t in tot]
    while True:
        if not tuples:
            print(str(1//0))
            exit()
        t = max(tuples,key = lambda x: match(tot_cop,x))
        tuples.remove(t)
        if d[t]:
            j = d[t].pop()
            break
    
    print(j+1,flush=True)
    update(j)
    
    
        
    
    


print(S)

    
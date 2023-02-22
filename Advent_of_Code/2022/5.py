import sys
tot = 0
stacks = [[] for _ in range(10)]
for line in sys.stdin.read().strip().split('\n'):
    #if tot < 10: print(line)
    if tot < 8:
        a = str(line)
        a = a.replace("[", " ")
        a = a.replace("]", " ")
        a = list(a.split())

    
    if tot < 8:
        for i in range(len(a)):
            if a[i] != ".":
                stacks[i+1].append(a[i])
            
        
    if tot == 8:
        print()
        for s in stacks:
            s.reverse()
        for l in stacks: print(l)
    tot += 1
    if tot >= 11:
        a = line.split()
        if tot <=15:
            print(a)
        #print(a)
        amount, fr, to = int(a[1]), int(a[3]), int(a[-1])
        for oper in range(amount):
            if len(stacks[fr]) >0:
                temp = stacks[fr].pop()
                stacks[to].append(temp)
        if tot <= 15:
            for l in stacks:
                print(l)
out = []
for s in stacks:
    if s:
        out.append(s[-1])
print(''.join(map(str,out)))
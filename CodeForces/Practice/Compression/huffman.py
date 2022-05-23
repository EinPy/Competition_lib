from collections import Counter

def huffman(text):
    freq = Counter(text)
    heap = []
    #print(freq)
    
    for i, (ch,v) in enumerate(freq.items()):
        heap.append((v, i, ch))
        #print(v,i,ch)
        
    idx = len(freq)
    while len(heap) > 1:
        heap.sort()
        e0, e1 = heap.pop(0), heap.pop(0)
        su = e0[0] + e1[0]
        heap.append((su, idx, (e0[2], e1[2])))
        idx += 1
        
    lookup = {}
    
    def trav(pref, tree):
        if type(tree) == str:
            lookup[tree] = pref
        else:
            trav(pref + '0', tree[0])
            trav(pref + '1', tree[1])
            
    trav('', heap[0][2])    
    #print(heap)
    return lookup
    
    
    
def encode(text, lookup):
    out = []
    for ch in text:
        out.append(lookup[ch])
    return ''.join(out)    

def decode(encoded, lookup):
    rev = {v : k for k, v in lookup.items()}
    out = []
    curr = ''
    for ch in encoded:
        curr += ch
        if curr in rev:
            out.append(rev[curr])
            curr = ''
    
    return ''.join(out)
 
    

f = open("compress.txt", "r")
inp = []
for _ in range(1000):
    inp.append(f.readline())

inp = ''.join(inp)
#print(inp)

lookup = huffman(inp)
enc = encode(inp, lookup)
dec = decode(enc, lookup)
print(lookup)
#print(dec)
print(enc)
newS = []
end = len(enc) % 8
multiples = len(enc) // 8
for i in range(multiples):
    p = i * 8
    slice = enc[p:p+8]
    n = (int(slice, 2))
    newS.append(n)
    
lastLength = 0
if end != 0:
    c = int(enc[multiples*8:],2)
    lastLength = len(str(c))
    newS.append(c)
    
print(newS)
get = newS
orgS = []
for i in range(len(get)):
    if i != len(get)-1:
        new = bin(int(get[i]))[2:]
        n = len(new)
        orgS.append((8-n)*'0' + new)
    else:
        if end:
            new = bin(int(get[i]))[2:]
            n = len(new)
            pad = max(0, end - n)
            orgS.append((pad)*'0' + new)
        else:
            new = bin(int(get[i]))[2:]
            n = len(new)
            orgS.append((8-n)*'0' + new)
        
    
print(orgS)

newByteArray = bytearray(newS)
    
orgS = ''.join(orgS)
print(orgS)
print(enc == orgS)
f = open("compressed.bin", "wb")
f.write(newByteArray)
f.close()
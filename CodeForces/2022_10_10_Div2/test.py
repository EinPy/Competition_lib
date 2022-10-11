def ok(n, a):
    if n == len(a):
        return True
    if n == 1:
        if len(set(a)) == 1:
            return True
    initial = 0
    for i in range(n):
        initial += a[i]
    #print(initial)
    ind = n
    #print("start at",ind)
    partSum = 0
    s = len(a)
    streak = 0
    while ind < s and partSum < initial and streak < n:
        
        #print(ind, partSum)
        partSum += a[ind]
        streak += 1
        if partSum == initial:
            ind += 1
            partSum = 0
            streak = 0
        else:
            ind += 1
            
    if partSum == 0:
        #print("first")
        return True
    
    #now for sliding window part
    #print("slide")
    for i in range(1, s - n + 1):
        #print(i, i+n-1)
        initial -= a[i-1]
        initial += a[i+n-1]
        #print(initial)
        #print("sum", initial)
        #one while loop before and one after
        pos = True
        ind = 0
        partSum = 0
        streak = 0
        while ind < i and partSum < initial and streak < n:
            #print(ind)
            partSum += a[ind]
            streak += 1
            if partSum == initial:
                ind += 1
                partSum = 0
                streak = 0
            else:
                ind += 1
        if partSum != 0: pos = False
        #print("after first", pos)
        if pos:
            #print("here")
            ind = i+ n
            #print("starting at", ind)
            partSum = 0
            streak = 0
            while ind < s and partSum < initial and streak < n:
                #print(ind)
                partSum += a[ind]
                streak += 1
                #print("ind", ind, partSum, streak)
                if partSum == initial:
                    ind += 1
                    partSum = 0
                else:
                    ind += 1
            if partSum != 0: pos = False
            if pos:
                return True
    return False
    
    



def ok2(n, a):
    if n == len(a):
        return True
    if n == 1:
        if len(set(a)) == 1:
            return True
        #else:return False
    s = len(a)
    for i in range(s - n + 1):
        r = i + n - 1
        targ = sum(a[i:r+1])
        possible = True
        #print(i, r, targ)
        if i != 0:
            ind = 0
            tot = 0
            streak = 0
            #print(ind, tot, streak)
            while ind < i and streak < n and tot < targ:
                #print(ind)
                tot += a[ind]
                streak += 1
                if tot == targ:
                    tot = 0
                    streak = 0
                ind += 1
            if tot != 0:
                possible = False
                p#rint("not possible")
        if r != s -1:
            ind = r + 1
            tot = 0
            streak = 0
            while ind < s and streak < n and tot < targ:
                #print(ind)
                tot += a[ind]
                streak += 1
                if tot == targ:
                    tot = 0
                    streak += 1
                ind += 1
            if tot != 0:
                possible = False
        if possible: return True
            
    return False
        
print(ok2(1, [55, 45, 30, 30, 40, 100]))
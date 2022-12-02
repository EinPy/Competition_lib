def getPrimesBelow(N):
    primes = []
    soll = [1]*N
    for p in range(2, N):
        if soll[p]:
            primes.append(p)
            for k in range(p*p, N, p):
                soll[k] = 0
    return primes

print(getPrimesBelow(12))

arr = [1, 2, 3, 4, 5, 6]
print(*arr)
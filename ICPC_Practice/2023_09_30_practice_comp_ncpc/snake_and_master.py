n = int(input())
mod = 10**6
arr = [0 for _ in range(n+2)]
arr[0],arr[1]  = 1, 1
if n == 1:
    print(1)
else:
    for i in range(2, n+2):
        arr[i] = (arr[i-2] + arr[i-1]) % mod
    print(arr[n])


R = int(input())
L = 1
found = False
days = 0
while not found:
    days += 1
    mid = (L + R) // 2 
    guess = mid * days
    print(guess, flush=True)
    a = input()
    if a == "less":
        R = mid - 1
    if a == "more":
        L = mid + 1
    if a == "exact":
        break
    
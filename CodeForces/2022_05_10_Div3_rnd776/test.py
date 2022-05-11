test = [3, 2, 5, 6, 1, 4]
newA = test[3+1:6+1] + test[:3] + [test[3]] + test[6:] 
print(test)
print(newA)
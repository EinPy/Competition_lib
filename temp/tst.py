print( min ( [(5, 'a'), (3, 'b')]))

a = [(5, 'a'), (3, 'b')]
a.pop(a.index(min(a)))
print(a)
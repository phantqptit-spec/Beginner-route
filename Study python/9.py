a = int(input('Number 1: '))
b = int(input('Number 2: '))
if a > b:
    A = True
else:
    A = False
if a >= b:
    B = True
else:
    B = False
print(A and B)
print(A or B)
print(not A)
print(not B) 
import random

n = random.randint(1, 10)
m = 0
while m != n:
    m = int(input('Đoán số:'))
    if n > m:
        print('Số lớn hơn')
    elif m > n:
        print('Số nhỏ hơn')
print('Chúc mừng')    

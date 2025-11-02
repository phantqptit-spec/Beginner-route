n = int(input('Nhập số n:'))
a = 0
for m in range(1,n+1):
    if m % 2 == 0:
        a += 1
print(f'Số số chẵn là:{a}')
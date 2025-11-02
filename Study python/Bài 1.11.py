number = int(input('Nhập một số n (1-9):'))
for i in range(1, 10):
    for n in range(1, number + 1):
        print(f'{n} x {i} = {i*n:<3}',end = '    ')
    print()
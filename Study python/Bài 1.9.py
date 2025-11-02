while True:
 klw = int(input('Số kWh tiêu thụ:'))
 if klw == 0:
    print('Nhập lại vì số tiền ko hợp lệ')
    continue
 elif klw <= 50:
   klw = klw * 1800
 elif 51 <= klw <= 100:
   klw = 50 * 1800 + (klw - 50) * 2000
 else:
   klw = 50 * 1800 + 50 * 2000 + (klw - 100) * 2500
 print(f'Tổng số tiền điện là: {klw}')
 break
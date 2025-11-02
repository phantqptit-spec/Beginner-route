dictionary = {'red':'đỏ','yellow':'vàng','green':'xanh lá cây', 'smart':'thông minh', 'bed':'giường'}
menu =  ('Từ điển Tiếng Anh'.center(27, '='), '1 - Tra từ điển' , '2 - Thêm từ điển' , '3 - Xóa từ điển' , '4 - Thoát chương trình')
while True:
    for u in menu:
       print(u)
    Input_number = int(input('Hãy ghi con số ứng với mục mà bạn muốn ở đây:'))
    if Input_number == 1:
      while True:
        tra_tu = input('Nhập từ tiếng anh cần tra ở đây hoặc nhập 0 để về menu:')
        if tra_tu == '0':
            break    
        elif dictionary.get(tra_tu.lower(),'') == '':
         #Áp dụng kết quả none đôi thành '' và so sánh để ra dưới          
            print('Không tìm thấy từ này trong từ điển')
        else:
            print(f'Nghĩa Tiếng Việt của từ {tra_tu} là: {dictionary.get(tra_tu.lower())}')
        tiep_tuc = True
        #Đặt tiep_tuc ở đây để nó luôn là true khi vòng lặp quay lại    
        while tiep_tuc:   
            your_choice = input('Bạn có muốn tra tiếp không? (y/n):')
            if your_choice == 'y':
                break
            elif your_choice != 'n' and your_choice != 'y':
                print('Chỉ có thể điền y hoặc n')
            else:
                tiep_tuc = False
            #Vì else chỉ kích hoạt khi ko break nên n -> menu    
        else:
            break  
    elif Input_number == 2:
        while True:
            eword = input('Nhập một từ tiếng Anh mà bạn muốn thêm vào hoặc nhập 0 để về menu:')
            if eword == '0':
                break
            Eword = eword.lower()  
            Vword = input('Nhập nghĩa tiếng Việt của từ đó:')
            if dictionary.get(Eword) == Vword.lower():
                print('Từ này đã có trong từ điển!')
            else:
                dictionary[Eword] = Vword.lower()
                print('Đã thêm thành công!')
            tiep_tuc = True
            while tiep_tuc:
                choice = input('Bạn có muốn thêm tiếp không? (y/n):')
                if choice != 'y' and choice != 'n': #Cấu trúc y/n y đúc đằng trên
                    print('Chỉ có thể điền y hoặc n')
                elif choice == 'y':
                    break
                else:
                    tiep_tuc = False
            else:
                break
    elif Input_number == 3:
        Delete_word = input('Nhập từ tiếng Anh muốn xóa hoặc nhập 0 để về menu')
        if Delete_word == 0:
            break
        elif dictionary.get(Delete_word.lower(), '') == '':
            print("Không tìm thấy từ cần xóa")
        else:
            del dictionary[Delete_word]
        tieptuc = True
        while tieptuc:
            choice = input('Bạn có muốn thêm tiếp không? (y/n):')
            if choice != 'y' and choice != 'n': #Cấu trúc y/n y đúc đằng trên
                print('Chỉ có thể điền y hoặc n')
            elif choice == 'y':
                break
            else:
                tiep_tuc = False
        else:
            break  
    elif Input_number == 4:
      print('Hẹn gặp lại bạn sau')
      break
    else:
      print('Xin hãy điền lại')

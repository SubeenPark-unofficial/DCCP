# TODO 1: Set a password and a pin code
password = 1234
pin = "python"

# TODO 2: Compare a password
count_password = 3
while count_password > 0:
    password_in = int(input("비밀번호를 입력하세요. "))
    if password_in == password:
        print ("잠금 해제되었습니다.")
        break
    else:
        count_password -= 1
        if count_password > 0:
            print (f"잘못된 비밀번호입니다. 남은 횟수는 {count_password} 회입니다.")
        else: 
            print ("잘못된 비밀번호입니다.")
        


# TODO 3: Compare a pin code
        
count_pin = 3
if count_password == 0:
    
    while count_pin > 0:
        
        pin_in = input("핀 코드를 입력하세요. ")
        
        if pin_in == pin:
            print ("잠금 해제되었습니다.")
            break
        
        else:
            count_pin -= 1
            if count_pin > 0:
                print (f"잘못된 핀 코드입니다. 남은 횟수는 {count_pin} 회입니다.")
            else: 
                print ("비활성화되었습니다.") 
            

    


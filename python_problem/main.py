num = 0

check = True
while check :
    userNum = input("부를 숫자의 개수를 입력하세요(1, 2, 3만 입력 가능) :")

    try:
        userNum = int(userNum)
        if userNum == 1 or userNum == 2 or userNum == 3:
            check = False
        else:
            print("1,2,3 중 하나를 입력하세요")
    except:
        print("정수를 입력하세요")

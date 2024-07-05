def brGame(mem):
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

    for i in range(userNum):
        num += 1
        print("playerA : " , num)
        if num == 31:
            print(mem, " win!")
            return False
    return True

num = 0
flag = True
while flag:

    players = ["playerA", "playerB"]
    for i in players:
        flag = brGame(i)
        if flag == False:
            break



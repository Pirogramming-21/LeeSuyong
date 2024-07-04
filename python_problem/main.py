num = 0

check = True
while check :
    userNum = int(input("부를 숫자의 개수를 입력하세요(1, 2, 3만 입력 가능) :"))
    if userNum != 1 & userNum != 2 & userNum != 3:
        continue
    else:
        check = False

import random


def brGame(mem, num):

    while True :
        #컴퓨터의 경우
        if i == "computer":
            userNum = random.randint(1,3)
            break
        #유저의 경우
        else:
            userNum = input("부를 숫자의 개수를 입력하세요(1, 2, 3만 입력 가능) :")

            try:
                userNum = int(userNum)
                if userNum == 1 or userNum == 2 or userNum == 3:
                    break;
                else:
                    print("1,2,3 중 하나를 입력하세요")
            except:
                print("정수를 입력하세요")

    #저장된 횟수만큼 반복한다.
    for j in range(userNum):
        num = printing(num, mem)
        if num == 31:
            return num
    return num

def printing(num, mem):
    num += 1
    print(i ," " , num)
    if num == 31:
        print(mem, " win!")
        return num
    return num


num = 0
while num != 31:

    players = ["computer", "player"]
    for i in players:
        num = brGame(i, num)
        if num == 31:
            break



num=int(input())
for i in range(num):
    for j in range(num+i):
        if num-i-1<=j:
            print('*',end='')
        else:
            print(' ',end='')
    print()
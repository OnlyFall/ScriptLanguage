N = 0
flag = True # 토글

for i in range(8):
    Board = input()
    for j in range(8):
        if flag: #짝수 인덱스가 흰색
            if j%2==0 and Board[j] =='F':
                N+=1
        else:
            if j%2==1 and Board[j] =='F':
                N+=1
    flag = not flag

print(N)

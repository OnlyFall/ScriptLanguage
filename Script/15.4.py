def m(i):
    if i == 1:
        return 1
    return 1/i + m(i-1)


t = eval(input("숫자 입력: "))

for i in range(1,t + 1,1):
    print("m(", i,"=)",m(i))
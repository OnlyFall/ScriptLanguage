l = [eval(i) for i in input("0~100 사이의 정수 입력: ").split()]

l2 = []

for i in l:
    if not i in l2:
        l2.append(i)

print(l2)

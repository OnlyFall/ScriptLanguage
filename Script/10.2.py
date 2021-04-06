l = [eval(i) for i in input("정수 여러개 입력: ").split()]

#l.reverse()
print(l)

for i in range(len(l) -1, -1, -1):
    print(l[i])

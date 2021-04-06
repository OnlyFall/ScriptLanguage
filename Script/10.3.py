l = [eval(i) for i in input("1~100 사이의 정수를 입력: ").split()]

d = {} # 빈 딕셔너리 :)

for i in l:
    if not i in d:
        d[i] = l.count(i)

keyList = list(d.keys())
keyList.sort()

for k in keyList:
    print("{0} - {1}번 나옴".format(k,d[k]))




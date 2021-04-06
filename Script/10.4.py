def average(list):
    sum = 0
    for i in range(len(list)):
        sum += list[i]
    return sum / len(list)



l = [eval(i) for i in input("1~100 사이의 점수를 입력: ").split()]

up = 0
down = 0
for i in l:
    if i >= average(l):
        up += 1
    else:
        down += 1


print("평균보다 높은사람 : {0}, 평균보다 낮은사람 : {1}".format(up,down))



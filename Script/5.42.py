import random
number = [0] * 4

for i in range(1000000):
    x = random.random() * 2 - 1
    y = random.random() * 2 - 1

    if x < 0:
        number[0] += 1
    elif x > 0 and y < 0:
        number[3] += 1
    else:
        y1 = -x + 1
        if y < y1:
            number[2] += 1
        else:
            number[1] += 1

print(number)
print("홀수 영역의 비율 : {0:.2f}%".format((number[0] + number[2]) / 1000000 * 100))
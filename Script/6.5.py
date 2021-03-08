def displaySortedNumbers(num1, num2, num3):
    temp = [num1, num2, num3]

    temp.sort()
    print("정렬된 숫자는 {0}, {1}, {2} 입니다.".format(temp[0], temp[1], temp[2]))


s = eval(input("3개의 숫자를 입력하여 주세요: "))

displaySortedNumbers(s[0], s[1], s[2])

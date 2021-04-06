def hanoi(ndisks, startPeg=1, endPeg=3):
    if ndisks:
        hanoi(ndisks - 1, startPeg, 6 - startPeg - endPeg)
        print(startPeg, "번 기둥의", ndisks, "번 원반을", endPeg, "번 기둥에 옮깁니다.")
        hanoi(ndisks-1, 6 - startPeg -endPeg, endPeg)


d = eval(input("디스크 갯수 입력: "))
hanoi(d)
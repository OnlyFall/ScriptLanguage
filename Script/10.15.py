def isSorted(lst):
    tmp = lst[:]
    lst.sort()
    if tmp == lst:
        return True
    else:
        return False

def main():
    lst = [eval(i) for i in input("정수 입력 : ").split()]

    result = isSorted(lst)

    if result:
        print("정렬되어 있습니다.")
    else:
        print("정렬되어 있지 않습니다.")


main()
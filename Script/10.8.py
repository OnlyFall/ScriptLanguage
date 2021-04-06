def indexOfsmallestElement(lst):
    index = 0
    value = lst[0]

    for i in range(1, len(lst)):
        if value > lst[i]:
            index = i
            value = lst[i]

    return index



def main():
    lst = [eval(i) for i in input("정수 리스트 입력: ").split()]
    index = indexOfsmallestElement(lst)

    print("가장 작은 원소 인덱스 : ",index)

main()

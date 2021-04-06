def sumColumn(n, column):
    result = 0

    for i in range(3):
        result += n[i][column]
    return result

def main():
    n = []
    for i in range(3):
        l = [eval(i) for i in input("3x4행렬의 "+str(i)+ "행 원소 입력: ").split()]
        n.append(l)

    for j in range(4):
        print("열 {0}번 원소의 총합은 : {1}".format(j, sumColumn(n,j)))


main()
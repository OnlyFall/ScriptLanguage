def reverse(m):
    for i in range(3):
        for j in range(i,3):
            m[i][j], m[j][i] = m[j][i], m[i][j]
    return m

def printMatrix(m):
    for i in range(3):
        for j in range(3):
            print("{0:.2f}".format(m[i][j]), end=" ")
        print()

def main():
    print("3x3 행렬 입력!")
    m = []

    for _ in range(3):
        l = [eval(i) for i in input().split()]
        m.append(l)
    printMatrix(m)
    reverse(m)

    for i in range(3):
        m[i].sort()

    reverse(m)
    print()
    printMatrix(m)

main()
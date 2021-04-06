def god(m,n):

    if m%n == 0:
        return n
    return god(n, m%n)


while True:
    m,n = eval(input("숫자 2개 입력: "))
    print("{0}과 {1}의 최대공약수 : {2}".format(m,n,god(m,n)))
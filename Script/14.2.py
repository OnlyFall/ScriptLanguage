def main():
    l = [eval(i) for i in input("정수를 입력: ").split()]
    d = {}

    for i in l:
        if not i in d:
            d[i] = 1
        else:
            d[i] += 1
    max_frequency = max(d.values())

    for k,v in d.items():
        if max_frequency == v:
            print("가장 많은 빈도수! : {0} - {1}번 나타남".format(k,v))



main()

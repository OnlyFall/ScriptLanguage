
while True:
    s = input("a, b, c를 입력하세요 (ax^2 + bx + c = 0) :")
    t = s.split()
    t = [eval(i) for i in t]

    r1 = (-t[1] + (t[1]**2 - 4 * t[0] * t[2])**0.5) / 2 * t[0]
    r2 = (-t[1] - (t[1]**2 - 4 * t[0] * t[2])**0.5) / 2 * t[0]

    temp = t[1]**2 -4 * t[0] * t[2]

    if r1 != r2 and temp >= 0:
        print("실근은 {0:.6f}과 {1:.6f} 입니다.".format(r1, r2))
    elif r1 == r2 and temp >= 0:
        print("실근은 {0:.6f} 입니다.".format(r1))
    else:
        print("이 방정식은 실근이 존재하지 않습니다.")


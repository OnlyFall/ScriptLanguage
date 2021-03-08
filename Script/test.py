x, y = eval(input("점 x,y 입력:"))

if 0 <= x <= 200 and 0 <= y <= 100:
    #직선 아래에 있는지 판단? y = -0.5x + 100
    #직선 위의 y값

    y1 = -0.5*x + 100
    if y <= y1:
        print("삼각형 내부에 있다")
    else:
        print("삼각형 외부에 있다")

else:
    print("삼각형 외부에 있다.")

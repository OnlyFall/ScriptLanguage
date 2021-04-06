
def main():
    x ,y = eval(input("x,y 좌표값 입력: "))
    if 0<x<200 and 0<y<100:

        y1 = -0.5*x + 100

        if y <= y1:
            print("삼각형 내부에 있다.")
        else:
            print("삼각형 외부에 있다.")


main()
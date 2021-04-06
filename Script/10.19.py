import random

def main():
    B = eval(input("공의 갯수 : "))
    S = eval(input("슬롯의 수 : "))

    slots = [0] * S

    for i in range(8):
        R = 0
        for j in range(S-1):
            if random.randint(0,1):
                R += 1
                print("R",end="")
            else:
                print("L",end="")
        print()
        slots[R] += 1

    m = max(slots)
    for i in range(m,0,-1):
        for j in range(S):
            if slots[j] < i:
                print(" ", end="")
            else:
                print("@", end="")
        print()


main()
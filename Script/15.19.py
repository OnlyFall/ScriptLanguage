def decimalToBinary(value):
    if value == 0:
        return ""
    return decimalToBinary(value//2) + str(value%2)


t = eval(input("숫자 입력: "))

print("결과: ", decimalToBinary(t))

def decimalToHex(value):
    if value == 0:
        return ""
    r = value % 16
    if r == 15:
        s = 'F'
    elif r == 14:
        s = 'E'
    elif r == 13:
        s = 'D'
    elif r == 12:
        s = 'C'
    elif r == 11:
        s = 'B'
    elif r == 10:
        s = 'A'
    else:
        s = str(r)
    return decimalToHex(value//16) + s

t = eval(input("값 입력: "))

print("결과: ", decimalToHex(t))
def reverse(number):
    temp = int(str(number)[::-1])
    return temp



def isPalindrome(number):
    t = reverse(number)
    if t == number:
        return True
    else:
        return False

s = eval(input("정수를 하나 입력하여 주세요: "))

t = reverse(s)
k = isPalindrome(s)

print("결과값:", t)

if k:
    print(s, "는 대칭수이다.")
else:
    print(s, "는 대칭수가 아니다.")
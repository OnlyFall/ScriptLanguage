def reverse(number):
    temp = int(str(number)[::-1])
    return temp



def isPalindrome(number):
    t = reverse(number)
    if t == number:
        return True
    else:
        return False


def isPrime(n):
    for i in range(2,n//2):
        if n%i ==0:
            return False
    return True




s = eval(input("정수를 하나 입력하여 주세요: "))

while(True):
    if isPalindrome(s) and isPrime(s):
        print(s)
        break
    s+=1
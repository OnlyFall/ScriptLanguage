import os

class Fan:
    def __init__(self, speed=1, radian=5, color="blue", isOn=False):
        self.speed = speed
        self.radian = radian
        self.color = color
        self.isOn = isOn

    def setSpeed(self, speed):
        self.speed = speed

    def setColor(self, color):
        self.color = color

    def setOnOff(self, isOn):
        self.isOn = isOn

    def setSize(self, radian):
        self.radian = radian

    def Show(self):
        print("속도: ", self.speed, ", 크기: ", self.radian, ", 색상 : ", self.color, ", 전원: ", self.isOn)


a = [0] * 2
for i in range(2):
    a[i] = Fan()

while(True):
    i = eval(input("어느 선풍기 옵션을 바꿀까요? : "))
    print("1. 팬 속도 조절 (1 ~ 3)")
    print("2. 선풍기 색상 조절")
    print("3. 선풍기 전원 설정")
    print("4. 선풍기 크기 조절")
    print("5. 모든 선풍기 정보 보기")
    t = eval(input("원하는 옵션을 선택하세요: "))

    if t == 1:
        k = eval(input("팬 속도를 1 ~ 3 사이로 입력: "))
        a[i - 1].setSpeed(k)
    elif t == 2:
        k = input("색상을 입력하세요: ")
        a[i - 1].setColor(k)
    elif t == 3:
        k = input("선풍기 전원 설정 On/Off 입력해 주세요: ")
        if k == 'On' or k == 'on':
            a[i - 1].setOnOff(True)
        elif k == 'Off' or k == 'off':
            a[i - 1].setOnOff(False)
    elif t == 4:
        k = eval(input("선풍기 사이즈를 입력하세요: "))
        a[i - 1].setSize(k)

    elif t == 5:
        for h in range(2):
            a[h].Show()


class Triangle:
    def __init__(self, side1=1.0, side2=1.0, side3=1.0, fill=1, color="blue"):
        self.side1 = side1
        self.side2 = side2
        self.side3 = side3
        self.fill = fill
        self.color = color

    def setSide1(self, side1):
        self.side1 = side1

    def setSide2(self, side2):
        self.side2 = side2

    def setSide3(self, side3):
        self.side3 = side3

    def setTriangle(self, side1, side2, side3, fill, color):
        self.side1 = side1
        self.side2 = side2
        self.side3 = side3
        self.fill = fill
        self.color = color

    def GetArea(self):
        self.t = (self.side1 + self.side2 + self.side3) / 2
        self.area = (self.t * (self.t - self.side1) * (self.t - self.side2) * (self.t - self.side3)) ** 0.5
        print("넓이 : ", self.area)

    def GetPerimeter(self):
        print("둘레의 길이 : ", self.side1 + self.side2 + self.side3)

    def __str__(self):
        return "Triangle: side1 = " + str(self.side1) + " , side2 = " + str(self.side2) + " , side3 = " + str(self.side3)

    def isFill(self):
        if self.fill == 0:
            return False
        else:
            return True

t = Triangle()

t.GetArea()
t.GetPerimeter()
o = t.__str__()
print(o)
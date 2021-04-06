class rectangle:
    def __init__(self,width=1,height=2):
        self.width = width
        self.height = height

    def getArea(self):
        return self.width * self.height

    def getPerimeter(self):
        return (self.width + self.height) * 2

    def info(self):
        print("width : {0:.2f}, height : {1:.2f}, area : {2:.2f}, perimeter : {3:.2f}".format(self.width, self.height, self.getArea(), self.getPerimeter()))


r1 = rectangle(4,10)
r1.info()

r2 = rectangle(3.5, 35.7)
r2.info()
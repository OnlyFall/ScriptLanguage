from datetime import datetime

class StopWatch:
    def __init__(self, startTime=0, endTime=0):
        self.startTime = startTime
        self.endTime = endTime

    def start(self):
        self.startTime = datetime.now()

    def stop(self):
        self.endTime = datetime.now()

    def getElapsedTime(self):
        print(self.endTime - self.startTime)



total = 0
k = StopWatch()
k.start()
for i in range(1000000):
    total += i
k.stop()
print(total)
k.getElapsedTime()
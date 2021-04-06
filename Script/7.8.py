from datetime import datetime
import time

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
for i in range(10):
    total += i
    time.sleep(1)

k.stop()
print(total)
k.getElapsedTime()
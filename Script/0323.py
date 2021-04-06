class CounterManager:
    insCount = 0

    def __init__(self):
        CounterManager.insCount += 1

    def PrintInstanceCount():
        print("InstanceCount : ", CounterManager.insCount)


p1 = CounterManager()
p2 = CounterManager()
p3 = CounterManager()

CounterManager.PrintInstanceCount()

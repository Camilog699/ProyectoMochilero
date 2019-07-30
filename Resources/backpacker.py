class Backpacker:
    def __init__(self, money, time):
        self.money = money
        self.time = time
        self.min = self.money * 0.40
        self.work = self.getWork()

    def getWork(self):
        if self.money < self.min:
            return True
        else:
            return False

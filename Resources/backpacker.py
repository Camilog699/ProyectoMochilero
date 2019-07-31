class Backpacker:
    def __init__(self, money, time):
        self.money = money
        self.moneyinit = money
        self.time = time
        self.min = self.moneyinit * 0.40
        self.work = self.getWork()

    def getWork(self):
        if self.money < self.min:
            return True
        else:
            return False

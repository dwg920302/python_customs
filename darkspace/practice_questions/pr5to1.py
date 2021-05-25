class Calculator(object):
    def __init__(self):
        self.value = 0

    def add(self, val):
        self.value += val

    @staticmethod
    def main():
        cal = UpgradeCalculator()
        cal.add(10)
        cal.minus(7)

        print(cal.value)

        cal = MaxLimitCalculator()
        cal.add(50)  # 50 더하기
        cal.add(60)

        print(cal.value)


class UpgradeCalculator(Calculator):
    def minus(self, val):
        self.value -= val


class MaxLimitCalculator(Calculator):
    def add(self, val):
        self.value += val
        if self.value > 100:
            self.value = 100


Calculator.main()

class GradAvg(object):
    def __init__(self):
        pass

    @staticmethod
    def main():
        class_a = [70, 60, 55, 75, 95, 90, 80, 80, 85, 100]
        sums = 0
        for i in class_a:
            print(i)
            sums += i
        print(sums/len(class_a))


GradAvg.main()

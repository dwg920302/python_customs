class Looping(object):
    def __init__(self):
        pass

    @staticmethod
    def main():
        res = 0
        for i in range(1, 100+1):
            res += i
            i += 1
        print(res)


Looping.main()

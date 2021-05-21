class NoSame(object):
    def __init__(self):
        pass

    @staticmethod
    def main():
        a = [1, 1, 1, 2, 2, 3, 3, 3, 4, 4, 5]
        s = set(a)
        res = list(s)
        print(res)


NoSame.main()

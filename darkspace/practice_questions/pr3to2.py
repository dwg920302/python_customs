class AAAPPP(object):
    def __init__(self):
        pass

    @staticmethod
    def main():
        res = 0
        i = 1
        while i <= 1000:
            if i % 3 == 0:
                res += i
            i += 1
        print(res)


AAAPPP.main()

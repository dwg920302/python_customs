'''
filter와 lambda를 사용하여 리스트 [1, -2, 3, -5, 8, -3]에서 음수를 모두 제거해 보자.
'''


class Maain(object):
    def __init__(self):
        pass

    @staticmethod
    def main():
        ls = [1, -2, 3, -5, 8, -3]
        print(ls)
        print(list(filter(lambda x: x > 0, ls)))


Maain.main()

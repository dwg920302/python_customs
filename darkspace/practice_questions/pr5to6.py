# map과 lambda를 사용하여 [1, 2, 3, 4] 리스트의 각 요솟값에 3이 곱해진 리스트 [3, 6, 9, 12]를 만들어 보자.

def x3(x):
    return x * 3

class Mabin(object):
    def __init__(self):
        pass

    @staticmethod
    def main():
        ls = [1, 2, 3, 4]
        print(list(map(x3, ls)))


Mabin.main()

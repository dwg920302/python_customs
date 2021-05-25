class OddIdentifier(object):
    def __init__(self):
        pass

    @staticmethod
    def main():
        num = int(input('숫자 입력 -> '))
        is_odd(num)


def is_odd(num):
    if num % 2 == 1:
        print(f'{num}은 홀수임')
    else:
        print(f'{num}은 짝수임')


OddIdentifier.main()

class NinetoNine(object):
    def __init__(self):
        pass

    @staticmethod
    def main():
        a = 2
        while a < 10:
            print(f'[{a} dan]')
            b = 1
            while b < 10:
                print(f'{a} x {b} = {a*b}')
                b += 1
            a += 1

            #  Trash code


NinetoNine.main()


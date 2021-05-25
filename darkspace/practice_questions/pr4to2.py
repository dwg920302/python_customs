class AllAvg(object):
    def __init__(self):
        pass

    @staticmethod
    def main():
        res = 0
        ls = []
        while 1:
            num = input('더할 수를 입력 (0 입력 시 종료) ->')
            if num == '0':
                break
            else:
                ls.append(num)

        for i in ls:
            res += int(i)
        print(f'{res/len(ls)}')


AllAvg.main()

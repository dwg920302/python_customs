class Cell(object):

    dc = {}

    def lists_to_dict(self):
        for i, j in [range(1, 9 + 1), range(2, 9 + 1)]:
            self.dc[i] = f'{i}*{j}={i*j}'
        print(self.dc)

    @staticmethod
    def main():
        c = Cell()
        c.lists_to_dict()


Cell.main()

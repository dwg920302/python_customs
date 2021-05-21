class Replacer:
    def __init__(self, dat):
        self.dat = dat

    def replacing(self):
        print('replacing?')
        

    def output(self):
        print(self.dat)

if __name__ == '_main__':
    a ="881220-1068234"
    r = Replacer(a)
    r.replacing()
    r.output()
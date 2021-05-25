class OddIdentifier:
    def iden(self, num):
        self.num = num
        while(num>1):
            num-=2
        if(num == 1):
            print(self.num, ' is odd number')
        else:
            print(self.num, 'is even number')

if __name__ == '__main__':
    o = OddIdentifier()
    o.iden(13)


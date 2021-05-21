class Sumnavg:
    def getGrade(self, kor, mat, eng):
        self.kor = kor
        self.mat = mat
        self.eng = eng

    def sum(self):
        return thr.kor+thr.mat+thr.eng

    def avg(self):
        result = thr.sum()/3
        return result

if __name__ == '__main__':
    thr = Sumnavg()
    thr.getGrade(80, 55, 75)
    print(thr.avg())

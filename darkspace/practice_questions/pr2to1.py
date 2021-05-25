class Sumnavg:
    def getGrade(self, kor, mat, eng):
        self.kor = kor
        self.mat = mat
        self.eng = eng

    @staticmethod
    def sum(thr):
        return thr.kor+thr.mat+thr.eng

    @staticmethod
    def avg(thr):
        result = thr.sum()/3
        return result

    @staticmethod
    def main():
        Sumnavg.getGrade(80, 55, 75)
        print(Sumnavg.avg())


Sumnavg.main()

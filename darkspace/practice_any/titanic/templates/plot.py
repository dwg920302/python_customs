from practice_any.titanic.models.dataset import Dataset
from practice_any.titanic.models.service import Service
import matplotlib.pyplot as plt
from matplotlib import font_manager, rc     # 한글 깨짐 방지
import seaborn as sns
rc('font', family=font_manager.FontProperties(fname='C:/Windows/Fonts/H2GTRE.ttf').get_name())

'''
Train의 column = Index(['PassengerId', 'Pclass', 'Name', 'Sex', 'Age', 'SibSp', 'Parch',
'Ticket', 'Fare', 'Cabin', 'Embarked'], dtype='object')
'''


class Plot(object):

    dataset: object = Dataset()
    service: object = Service()

    def __init__(self, fname):
        self.dataset.fname = fname
        self.entity = self.service.new_model(self.dataset.fname)

    def plot(self):
        this = self.entity
        print(f'Train Type = {type(this)}')
        print(f'Train의 column = {this.columns}')
        print(f'Train의 상위 5개 데이터 = {this.head()}')
        print(f'Train의 하위 5개 데이터 = {this.tail()}')

    def draw_survived(self):
        this = self.entity  # entity를 복사해서 복사본으로 작업함. 원본은 타격 X
        f, ax = plt.subplots(1, 2, figsize=(18, 8))     #
        this['Survived'].value_counts().plot.pie(explode=[0, 0.1], autopct='%1.1f%%', ax=ax[0], shadow=True)
        ax[0].set_title('0.사망자 vs 1.생존자')
        ax[0].set_ylabel('')
        ax[1].set_title('0.사망자 vs 1.생존자')
        sns.countplot('Survived', data=this, ax=ax[1])
        plt.show()

    def draw_pclass(self):
        this = self.entity
        this['Pclass'] = this['Pclass'].replace(1, "1등석").replace(2, "비지니스").replace(3, "이코노미")     # 내용물 일괄 바꾸기
        sns.countplot(data=this, x="Pclass")
        plt.show()
        # 승객을 티켓(1,2,3등석 등)에 따라서 구분하는 차트 작성

    def draw_sex(self):
        this = self.entity
        sns.countplot(data=this, x="Sex")   # 굳이 바꾸지 않아도 상관없이 잘 나옴
        plt.show()
        # 승객의 성별에 따른 분류

    def draw_gender(self):
        this = self.entity
        axs = plt.subplot()
        this['Sex'].value_counts().plot.pie(explode=[0, 0.1], autopct='%1.1f%%')
        axs.set_title('생존자 성별비')
        axs.set_ylabel('')
        plt.show()
        # sns는 쓰기가 너무 쉬운데 plt를 생으로 쓰는건 뭣같음

    def draw_embarked(self):
        this = self.entity
        this['Embarked'] = this['Embarked'].replace('C', "Cherbourg").replace('Q', "QueensTown").replace('S', "Southampton")
        sns.countplot(data=this, x="Embarked")
        plt.show()
        # 해당 승객이 어떤 부두에서 탔는가에 따른 분류

    def draw_embarked_oth(self):
        this = self.entity
        axs = plt.subplot()
        this['Embarked'].value_counts().plot.barh()
        axs.set_title('(blank)')
        plt.show()

    def draw_four(self):
        this = self.entity
        this['Survived'].replace(1, "Survived").replace(0, "Dead")
        fig, axs = plt.subplots(1, 4, figsize=(18, 6))
        this['Survived'].value_counts().plot.pie(explode=[0, 0.2], autopct='%1.1f%%', ax=axs[0])
        axs[0].set_title('Survivors')
        this['Pclass'] = this['Pclass'].replace(1, "1등석").replace(2, "비지니스").replace(3, "이코노미")     # 내용물 일괄 바꾸기
        sns.countplot(data=this, x="Pclass", ax=axs[1])
        this['Sex'].value_counts().plot.pie(explode=[0, 0.1], autopct='%1.1f%%', ax=axs[2])
        axs[2].set_title('생존자 성별비')
        axs[2].set_ylabel('')
        this = self.entity
        this['Embarked'] = this['Embarked'].replace('C', "Cherbourg").replace('Q', "QueensTown").replace('S', "Southampton")
        this['Embarked'].value_counts().plot.barh(ax=axs[3])
        plt.show()

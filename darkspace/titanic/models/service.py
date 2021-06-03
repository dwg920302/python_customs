from titanic.models.dataset import Dataset
import pandas as pd
import numpy as np
from sklearn.svm import SVC
from sklearn.model_selection import KFold
from sklearn.model_selection import cross_val_score


def binary(val):
    if val >= 1:
        return 1
    else:
        return 0


def lastcvt(val):
    if val is str:
        return 1
    else:
        return 0


class Service(object):
    dataset = Dataset()

    def new_model(self, payload):
        this = self.dataset
        this.context = './data/'
        this.fname = payload
        return pd.read_csv(this.context + this.fname)

    @staticmethod
    def create_train(this) -> object:
        return this.train.drop('Survived', axis=1)  # 0 = 가로 1 = 세로

    @staticmethod
    def create_label(this) -> object:
        return this.train['Survived']

    @staticmethod
    def drop_feature(this, *features) -> object:
        for i in features:
            this.train = this.train.drop([i], axis=1)
            this.test = this.test.drop([i], axis=1)
        return this

    @staticmethod
    def create_k_fold() -> object:
        return KFold(n_splits=10, shuffle=True, random_state=0, n_jobs=10)

    @staticmethod
    def accuracy_by_svm(this):
        score = cross_val_score(SVC(),
                                this.train,
                                this.label,
                                cv=KFold(n_splits=10, shuffle=True, random_state=0),
                                n_jobs=10,
                                scoring='accuracy')
        return round(np.mean(score) * 100, 2)

    # 이 밑에 메소드 입력

    @staticmethod
    def pclass_nominal(this) -> object:
        #1등석은 냅두고 나머지는 전부 0 처리함
        dict_pc = {1: 1, 2: 0, 3: 0}
        for data in [this.train, this.test]:
            data = data.fillna({'Pclass': 0})
            data['Pclass'] = data['Pclass'].map(dict_pc)
        return this

    @staticmethod
    def title_nominal(this) -> object:
        # Name을 Title로 바꾸고, 부유층을 전부 1로, 일반 남성과 미혼 여성은 2, 기혼 여성은 3으로 묶음. 0은 호칭이 없는 최하층
        title_mapping = {'Mr': 2, 'Miss': 2, 'Mrs': 3, 'Master': 1, 'Royal': 1, 'Rare': 1}
        combine = [this.train, this.test]
        for dataset in combine:
            dataset['Title'] = dataset.Name.str.extract('([A-Za-z]+)\.', expand=False)
            # 칼럼 추가방법. extract 내에 있는 건 정규표현식
            dataset['Title'] = dataset['Title'].replace(['Capt', 'Col', 'Don', 'Dr', 'Major', 'Rev', 'Jonkheer', 'Dona'], "Rare")
            dataset['Title'] = dataset['Title'].replace(['Countess', 'Lady', 'Sir'], 'Royal')
            dataset['Title'] = dataset['Title'].replace('Mlle', 'Mr')
            dataset['Title'] = dataset['Title'].replace('Ms', 'Miss')
            dataset['Title'] = dataset['Title'].replace('Mme', 'Rare')
            dataset['Title'] = dataset['Title'].fillna(0)
            dataset['Title'] = dataset['Title'].map(title_mapping)
        return this

    @staticmethod
    def gender_nominal(this) -> object:
        # 남자는 0, 여자는 1로 나눔
        mapping = {'male': 0, 'female': 1}
        combine = [this.train, this.test]
        for dataset in combine:
            dataset.rename(columns={'Sex': 'Gender'}, inplace=True)
            dataset['Gender'] = dataset['Gender'].map(mapping)
        return this

    @staticmethod
    def age_ordinal(this) -> object:
        # 나이불명(-0.5)-> 0, ~18 -> 1, ~35 -> 2, ~60 -> 3, 60~ -> 4으로 구분
        bins = [-1, 0, 18, 35, 60, np.inf]
        labels = ['Unknown', 'Immature', 'Mature', 'Adult', 'Senior']
        age_title_mapping = {'Unknown': 0, 'Immature': 1, 'Mature': 2, 'Adult': 3, 'Senior': 4}
        combine = [this.train, this.test]
        for data in combine:
            data['Age'] = data['Age'].fillna(-0.5)  # -0.5 = Unknown
            data['AgeGroup'] = pd.cut(data['Age'], bins=bins, labels=labels)  # 이름이 같으면 bins=bins를 bins로 생략 안됨 ㅡㅡ
            data['AgeGroup'] = data['AgeGroup'].map(age_title_mapping)
            # data['Age'] = data['Age'].map(lambda a: int(a))   # 정수화 (소수점 버림)
        return this

    @staticmethod
    def sibspparch_ordinal(this) -> object:
        # 0은 0으로 맞추고, 1 이상 수치를 전부 1로 고정함
        for data in [this.train, this.test]:
            data['SibSp'] = data['SibSp'].map(lambda a: binary(a))
            data['Parch'] = data['Parch'].map(lambda a: binary(a))
        # 두 컬럼을 비교하고 높은 수치로 맞춤 (아직 작성 못함)
        return this

    @staticmethod
    def cabin_nominal(this) -> object:
        # A부터 B갑판 -> 1 C부터 D -> 2 나머지 0
        cab_mapping = {'A': 1, 'B': 1, 'C': 2, 'D': 2, 'E': 0, 'F': 0, 'G': 0, 0: 0}
        for data in [this.train, this.test]:
            data['Location'] = data['Cabin'].str.extract('([A-Z])', expand=False)
            data['Location'] = data['Location'].fillna(0)
            data['Location'] = data['Location'].map(cab_mapping)
            data['Location'] = data['Location'].map(lambda a: lastcvt(a))
        return this

    @staticmethod
    def embarked_nominal(this) -> object:
        # S와 C는 그냥 평범한 항구도시 -> 0 Q는 부자동네 -> 1
        this.train = this.train.fillna({'Embarked': 'S'})
        this.test = this.test.fillna({'Embarked': 'S'})
        dict_em = {'S': 0, 'C': 0, 'Q': 1}
        this.train['Embarked'] = this.train['Embarked'].map(dict_em)
        this.test['Embarked'] = this.test['Embarked'].map(dict_em)
        #   map 함수를 사용하여, S : 1, C : 2, Q : 3
        return this

from titanic.models.dataset import Dataset
import pandas as pd
import numpy as np
from sklearn.svm import SVC
from sklearn.model_selection import KFold
from sklearn.model_selection import cross_val_score


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
    def embarked_nominal(this) -> object:
        this.train = this.train.fillna({'Embarked': 'S'})
        this.test = this.test.fillna({'Embarked': 'S'})
        dict_em = {'S': '1', 'C': '2', 'Q': '3'}
        this.train['Embarked'] = this.train['Embarked'].map(dict_em)
        this.test['Embarked'] = this.test['Embarked'].map(dict_em)
        #   map 함수를 사용하여, S : 1, C : 2, Q : 3
        return this

    @staticmethod
    def fare_ordinal(this) -> object:
        this.test['Fare'] = this.test['Fare'].fillna(1)

        fare_mapping = {'C': 1, 'B': 2, 'A': 3, 'S': 4}
        bins = [-1, 8, 13, 30, np.inf]
        labels = ['S', 'A', 'B', 'C']
        for data in [this.train, this.test]:
            data['FareBand'] = pd.cut(data['Fare'], bins=bins, labels=labels)
            data['FareBand'] = data['FareBand'].map(fare_mapping)
        return this

    @staticmethod
    def title_nominal(this) -> object:
        title_mapping = {'Mr': 1, 'Miss': 2, 'Mrs': 3, 'Master': 4, 'Royal': 5, 'Rare': 6}
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
            #fillna(0) 0은 호칭이 없는 극빈, 노예
        return this

    @staticmethod
    def gender_nominal(this) -> object:
        mapping = {'male': 0, 'female': 1}
        combine = [this.train, this.test]
        for dataset in combine:
            dataset.rename(columns={'Sex': 'Gender'}, inplace=True)
            dataset['Gender'] = dataset['Gender'].map(mapping)
            # 만약 inplace=True가 없다면 바뀐 내용이 적용되지 않음
        return this

    @staticmethod
    def age_ordinal(this) -> object:
        bins = [-1, 0, 5, 12, 18, 24, 35, 60, np.inf]   # 어린이, 성인, 중년, 노인 등 구분하는 거 같음
        labels = ['Unknown', 'Baby', 'Child', 'Teenager', 'Student', 'Young Adult', 'Adult', 'Senior']
        age_title_mapping = {'Unknown': 0, 'Baby': 1, 'Child': 2, 'Teenager': 3, 'Student': 4, 'Young Adult': 5,
                             'Adult': 6, 'Senior': 7}
        combine = [this.train, this.test]
        for data in combine:
            data['Age'] = data['Age'].fillna(-0.5)  # -0.5 = Unknown
            data['AgeGroup'] = pd.cut(data['Age'], bins=bins, labels=labels)  # 이름이 같으면 bins=bins를 bins로 생략 안됨 ㅡㅡ
            data['AgeGroup'] = data['AgeGroup'].map(age_title_mapping)
            # data['Age'] = data['Age'].map(lambda a: int(a))   # 정수화 (소수점 버림)
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

from titanic.models.dataset import Dataset
from titanic.models.service import Service
import pandas as pd
from sklearn.ensemble import RandomForestClassifier


class Controller(object):

    dataset: object = Dataset()
    service: object = Service()

    def modeling(self, train, test):
        service = self.service
        this = self.preprocess(train, test)
        this.label = service.create_label(this)
        this.train = service.create_train(this)
        return this

    def learning(self, train, test):
        this = self.modeling(train, test)
        print(f'사이킷런의 SVC 알고리즘 정확도 {self.service.accuracy_by_svm(this)} %')

    def submit(self, train, test):
        this = self.modeling(train, test)
        clf = RandomForestClassifier()
        clf.fit(this.train, this.label)
        prediction = clf.predict(this.test)
        pd.DataFrame({'PassengerId': this.id, 'Survived': prediction}).to_csv('./data/submission.csv', index=False)

    def preprocess(self, train, test):
        service = self.service
        this = self.dataset
        this.train = service.new_model(train)
        this.test = service.new_model(test)
        this.id = this.test['PassengerId']
        #   여기 밑에 조정할 것 입력
        this = service.pclass_nominal(this)
        this = service.title_nominal(this)
        this = service.gender_nominal(this)
        this = service.age_ordinal(this)
        this = service.sibspparch_ordinal(this)
        this = service.cabin_nominal(this)
        this = service.embarked_nominal(this)
        #   불필요한 feature 제거
        this = service.drop_feature(this, 'Name', 'Ticket', 'Fare', 'Cabin', 'Age')
        #   여기 위에 조정할 것 입력
        self.print_this(this)
        return this

    @staticmethod
    def print_this(this):
        combine = [this.train, this.test]
        print('-'*44+'<type check>'+'-'*44)
        for data in combine:
            print(f'type = {type(data)}')
            print(f'column = {data.columns}')
            print(f'상위 3개 데이터 = {data.head(3)}')
            print(f'null 갯수 = {data.isnull().sum()}')
        print('-' * 100)

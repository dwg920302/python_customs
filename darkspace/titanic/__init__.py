from titanic.views.controller import Controller
from titanic.templates.plot import Plot

if __name__ == '__main__':
    controller = Controller()
    while 1:
        mn = input('[Menu] (0)Exit (1)Data Visualization (2)Data Modeling '
                   '(3)Machine Learning (4)Machine Release -> ')
        if mn == '0':
            break
        elif mn == '1':
            plot = Plot('train.csv')
            plot.draw_survived()
            plot.draw_pclass()
            plot.draw_gender()
            plot.draw_embarked_oth()
        elif mn == '2':
            dat = controller.modeling('train.csv', 'test.csv')
        elif mn == '3':
            controller.learning('train.csv', 'test.csv')
        elif mn == '4':
            controller.submit('train.csv', 'test.csv')
        elif mn == '8':
            plot = Plot('train.csv')
            plot.draw_four()
        else:
            print('error')

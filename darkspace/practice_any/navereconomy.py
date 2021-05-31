import pandas as pd
from bs4 import BeautifulSoup
import urllib
from urllib.request import urlopen


class NaverEconomy(object):
    url = 'https://finance.naver.com/sise/lastsearch2.nhn'   # URL이 고정값이라 따로 입력받지 않음
    header = {'User-Agent': 'Mozilla/5.0'}
    path = './csv_data/naver_finance.csv'
    soup = None

    doc = ''

    ls_keys = []
    ls_values = []

    ls_indexes = []

    common_dict = {}
    common_dframe = None

    def get_stock_info(self):
        modifier = urllib.request.Request(self.url, headers=self.header)
        self.soup = BeautifulSoup(urlopen(modifier), "lxml")
        top30 = self.soup.select('#popularItemList > li > a')
        print(type(top30))
        print(top30)

        #   select가 막힌 거 같음 (추정)

    def get_csv(self):
        self.common_dframe = pd.DataFrame(self.common_dict)
        self.common_dframe.to_csv(self.path)

    @staticmethod
    def main():
        naver = NaverEconomy()
        while 1:
            menu = input('[Menu] \n[1 = get Stocks] [0 = Exit]')
            if menu == '0':
                break
            elif menu == '1':
                naver.get_stock_info()
            elif menu == '2':
                naver.get_csv()
            elif menu == '3':
                pass
            else:
                pass


NaverEconomy.main()

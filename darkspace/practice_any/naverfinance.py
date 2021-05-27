from bs4 import BeautifulSoup
import pandas as pd
import urllib
from urllib.request import urlopen
import requests


class NaverFinance(object):

    url = 'https://finance.naver.com/sise/lastsearch2.nhn'   # URL이 고정값이라 따로 입력받지 않음
    header = {'User-Agent': 'Mozilla/5.0'}
    path = './data/naver_finance.csv'
    soup = None

    doc = ''

    ls_keys = []
    ls_values = []
    ls_elements = []
    common_dict = {}
    common_dframe = None

    def set_soup(self):
        pass

    # 네이버 금융서버에서 http 패킷 헤더의 웹 브라우저 정보(User-agent)를 체크
    # 웹 브라우저 정보를 함께 전송해야 한다.

    def get_stock_info(self):
        print(self.url)
        with requests.get(self.url, self.header) as doc:
            html = BeautifulSoup(doc.text, "lxml")
            for i in html.find_all(name="tr"):
                if i == None:
                    continue
                else:
                    self.ls_keys.append(i.find(name='td', attrs=({"class": "no"})))
            print(self.ls_keys)

        # for i in self.soup.find_all(name="tr"):
        #     self.ls_keys.append(i.find(name='td', attrs=({"class": "no"})).text)
        # print(self.ls_keys)
        # text 빼면 잘 받아오긴 함, None이 마이 섞여있음; 이걸 처리해야 함

        # for i in self.soup.find_all(name="tr"):
        #     ls.append(i.find(name='a', attrs=({"class": "title"})).text)
        # print(ls)
        # 왜 자꾸 NoneType를 받는것인가... 위의 코드에서 못 받아온 건가?

    def get_what(self):
        pd.DataFrame.to_csv(self.path, sep=',', na_rep='NaN')

    @staticmethod
    def main():
        naver = NaverFinance()
        while 1:
            menu = input('[Menu] \n[1 = get Stocks] [0 = Exit]')
            if menu == '0':
                break
            elif menu == '1':
                naver.get_stock_info()
            elif menu == '2':
                naver.get_stock_info()
            elif menu == '3':
                pass
            else:
                pass


NaverFinance.main()

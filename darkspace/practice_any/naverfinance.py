from bs4 import BeautifulSoup
import pandas as pd
import requests


class NaverFinance(object):

    url = 'https://finance.naver.com/sise/lastsearch2.nhn'   # URL이 고정값이라 따로 입력받지 않음
    header = {'User-Agent': 'Mozilla/5.0'}
    path = './csv_data/naver_finance.csv'
    soup = None

    doc = ''

    ls_keys = []
    ls_values = []
    ls_elements = []

    ls_indexes = []

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
            for i in html.find_all(name='tr', attrs=({"class": "type1"})):
                try:
                    self.ls_indexes.append(i.find(name='th').text)
                except AttributeError:  # None 처리
                    continue
        print(self.ls_indexes)

        with requests.get(self.url, self.header) as doc:    # 이렇게 되어야만 동작함
            html = BeautifulSoup(doc.text, "lxml")
            for i in html.find_all(name="tr"):
                try:
                    self.ls_keys.append(i.find(name='td', attrs=({"class": "no"})).text)
                    self.ls_values.append([i.find(name='a', attrs=({"class": "tltle"})).text])
                except AttributeError:  # None-type 가져올 때 Error를 무시시킴
                    continue
                # 종목명 이름 TITLE(title)을 일부러 TLTLE(tltle)로 오타낸거 실화냐 ㅡㅡ
        print(self.ls_keys)
        print(self.ls_values)
        for i in range(len(self.ls_keys)):
            self.common_dict[self.ls_keys] = self.ls_values

    def get_csv(self):
        self.common_dframe = pd.DataFrame
        self.common_dframe.to_csv(self.path, sep=',', na_rep='NaN')


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
                naver.get_csv()
            elif menu == '3':
                pass
            else:
                pass


NaverFinance.main()

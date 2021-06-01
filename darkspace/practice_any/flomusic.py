from bs4 import BeautifulSoup
import urllib
from urllib.request import urlopen
import json


class Flo(object):

    url = 'https://www.music-flo.com/browse?chartId=1'
    header = {'User-Agent': 'Mozilla/5.0'}  # 저는 봇이 아닙니다 준비과정 01
    soup = ''
    lst = []

    def openurl(self):
        modifier = urllib.request.Request(self.url, headers=self.header)
        self.soup = BeautifulSoup(urlopen(modifier), 'lxml')
        print(self.url)

    def title_list(self):
        print(self.soup)

    @staticmethod
    def main():
        flo = Flo()
        while 1:
            mn = input('[Menu] (0)Exit -> ')
            if mn == '0':
                break
            elif mn == '1':
                flo.openurl()
            elif mn == '2':
                pass
            else:
                print('error')


Flo.main()
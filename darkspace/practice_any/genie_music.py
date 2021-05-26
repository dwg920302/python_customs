from bs4 import BeautifulSoup
from urllib.request import urlopen
import urllib.request


# 이 코드를 짜고 느낀 점 : 역시 벅스가 보안이 부실함;
# 공백을 없애는 작업이 필요 : 아직 수정 안함
# TOP 100이 아니라 50이 나옴 (원래 사이트 구성이 그런 거 같음)


class GenieMusic(object):
    url = 'https://www.genie.co.kr/chart/top200?ditc=D&ymd=20210525&rtm=Y&hh=18'
    header = {'User-Agent': 'Mozilla/5.0'}  # 저는 봇이 아닙니다 준비과정 01
    soup = ''

    date = ''
    hour = ''

    t_lst = []
    a_lst = []
    class_dict = {0: "title", 1: "artist"}
    common_dict = {}

    def set_url(self):

        self.url = f'https://www.genie.co.kr/chart/top200?ditc=D&ymd={self.date}&rtm=Y&hh={self.hour}'
        modifier = urllib.request.Request(self.url, headers=self.header)
        self.soup = BeautifulSoup(urlopen(modifier), 'lxml')

    def scrap(self):

        print(self.url)
        cnt = 0
        for i in self.soup.find_all(name='td', attrs=({"class": "info"})):
            cnt += 1
            title = i.find(name='a', attrs=({"class": "title ellipsis"})).text
            artist = i.find(name='a', attrs=({"class": "artist ellipsis"})).text
            print(f'{title} / {artist} / {cnt}위')
            # 되긴 하는데 띄어쓰기 때문에 이상하게 나옴

    def get_lists(self):
        for i in self.soup.find_all(name='td', attrs=({"class": "info"})):
            self.t_lst.append(i.find(name='a', attrs=({"class": "title ellipsis"})).text)
            self.a_lst.append(i.find(name='a', attrs=({"class": "artist ellipsis"})).text)

    def get_dict(self):
        self.get_lists()
        for i in range(len(self.t_lst)):
            self.common_dict[self.t_lst[i]] = self.a_lst[i]
        print(self.common_dict)
        # 되긴 하는데 띄어쓰기 때문에 이상하게 나옴

    @staticmethod
    def main():
        genie = GenieMusic()
        while 1:
            menu = input('[Menu] \n[1 = set URL] [2 = get Ranking] [0 = Exit]')
            if menu == '0':
                break
            elif menu == '1':
                genie.date = input('일자 입력 (ex) 20210525 -> ')
                genie.hour = input('몇 시의 차트를 보시겠습니까? -> ')
                genie.set_url()
            elif menu == '2':
                genie.scrap()
            elif menu == '3':
                genie.get_dict()
            else:
                pass


GenieMusic.main()

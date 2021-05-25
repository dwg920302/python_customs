from bs4 import BeautifulSoup
from urllib.request import urlopen
import urllib.request


# 이 코드를 짜고 느낀 점 : 역시 벅스가 보안이 부실함;
# 공백을 없애는 작업이 필요 : 아직 수정 안함
# TOP 100이 아니라 50이 나옴 (원래 사이트 구성이 그런 거 같음)


class GenieMusic(object):
    url = 'https://www.genie.co.kr/chart/top200?ditc=D&ymd=20210525&rtm=Y&pg=1'
    header = {'User-Agent': 'Mozilla/5.0'}  # 저는 봇이 아닙니다 준비과정 01

    def scrap(self):
        modifier = urllib.request.Request(self.url, headers=self.header)
        soup = BeautifulSoup(urlopen(modifier), 'lxml')
        print(self.url)
        cnt = 0
        for i in soup.find_all(name='td', attrs=({"class": "info"})):
            cnt += 1
            title = i.find(name='a', attrs=({"class": "title ellipsis"})).text
            artist = i.find(name='a', attrs=({"class": "artist ellipsis"})).text
            print(f'{title} / {artist} / {cnt}위')

    @staticmethod
    def main():
        genie = GenieMusic()
        while 1:
            menu = input('[Menu] \n[1 = get Ranking] [0 = Exit]')
            if menu == '0':
                break
            elif menu == '1':
                genie.scrap()
            elif menu == '2':
                print('fake menu')
            else:
                pass


GenieMusic.main()

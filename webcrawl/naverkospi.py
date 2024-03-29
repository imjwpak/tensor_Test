from bs4 import BeautifulSoup
import urllib.request as url

class NaverKospiCrawler:
    def __init__(self, param):
        self.param = param

    def scrap(self):
        html = url.urlopen(self.param).read()
        soup = BeautifulSoup(html, 'html.parser')
        txt = soup.find(id = 'KOSPI_now').text
        print('코스피 : ' + txt)

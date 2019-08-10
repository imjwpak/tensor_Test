from bs4 import BeautifulSoup
from urllib.request import urlopen

class StockCrawler:
    def __init__(self, item):
        self.item = item

    def scrap(self):
        url = f'https://finance.naver.com/item/sise_day.nhn?code={self.item}'
        # class="tah p11"
        soup = BeautifulSoup(urlopen(url), 'html.parser')

        for i in soup.find_all(name='span', attrs=({'class':'tah p11'})):
            print('종가 : ' + str(i.text))

from bs4 import BeautifulSoup
from selenium import webdriver

class NaverMovieCrawler:
    def __init__(self, url):
        driver = webdriver.Chrome(executable_path='C:/Users/ezen/PycharmProjects/tensorflow190803/webcrawl/data/chromedriver')
        driver.get(url)
        self.soup = BeautifulSoup(driver.page_source, 'html.parser')

    def scrap(self):
        html = self.soup.prettify()
        print(html)


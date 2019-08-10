from webcrawl.bugsmusic import BugsCrawler
from webcrawl.assembly import AssemblyCrawler
from webcrawl.naverkospi import NaverKospiCrawler
from webcrawl.krx import KrxCrawler
from webcrawl.naver_stock import StockCrawler
from webcrawl.naver_movie import NaverMovieCrawler
from webcrawl.naver_login import NaverLogin

class Controller:
    def __init__(self):
        pass

    def exec(self, flag):
        if flag == 'a':
            ab = AssemblyCrawler('http://likms.assembly.go.kr/bill/billDetail.do?billId=PRC_R1N9J0N1X0Y9A1O8S3R5Z3J3K9O8N7')
            ab.scrap()

        elif flag == 'b':
            bm = BugsCrawler('https://music.bugs.co.kr/chart/track/realtime/total?chartdate=20190810&charthour=11')
            bm.scrap()

        elif flag == 'p':
            nK = NaverKospiCrawler('https://finance.naver.com/sise/')
            nK.scrap()

        elif flag == 'k':
            kr = KrxCrawler('http://kind.krx.co.kr/disclosureSimpleSearch.do?method=disclosureSimpleSearchMain')
            kr.scrap()

        elif flag == 's':
            st = StockCrawler('005930')
            st.scrap()

        elif flag == 'm':
            nm = NaverMovieCrawler('https://movie.naver.com/movie/sdb/rank/rmovie.nhn')
            nm.scrap()

        elif flag == 'l':
            nl = NaverLogin('https://nid.naver.com/nidlogin.login')
            nl.auto_login()

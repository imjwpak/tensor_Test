from webcrawl.bugsmusic import BugsCrawler
from webcrawl.assembly import AssemblyCrawler

class Controller:
    def __init__(self):
        pass

    def exec(self,flag):
        if flag == 'a':
            as = AssemblyCrawler('http://likms.assembly.go.kr/bill/billDetail.do?billId=PRC_R1N9J0N1X0Y9A1O8S3R5Z3J3K9O8N7')
            as.scrap()

        elif flag == 'b':
            bm = BugsCrawler('https://music.bugs.co.kr/chart/track/realtime/total?chartdate=20190810&charthour=11')
            bm.scrap()

        return result
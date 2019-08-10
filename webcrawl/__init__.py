from webcrawl.controller import Controller

if __name__ == '__main__':
    print('a. 국회 크롤링')
    print('b. Bugs 크롤링')
    print('p. Naver Kospi 크롤링')
    print('s. Naver Stock 크롤링')
    print('m. Naver Movie 크롤링')
    print('k. KRX 크롤링')
    print('q. 종료')

    flag = input('flag 입력 : ')

    cntl = Controller()
    cntl.exec(flag)
    



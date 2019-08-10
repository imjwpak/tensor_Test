# calculator.model 모듈
# CalculatorModel 클래스
# calc 인스턴스
# CalculatorModel() 생성자
'''
from calculator.model import CalculatorModel

if __name__ == '__main__':
    num1 = int(input('첫 번째 수 : '))
    num2 = int(input('두 번째 수 : '))

    calc = CalculatorModel(num1, num2)
    result = calc.add()

    print('계산결과 %d ' % result)
'''
from calculator.controller import CalculatorController

if __name__ == '__main__':
    num1 = int(input('첫 번째 수 : '))
    num2 = int(input('두 번째 수 : '))

    c = CalculatorController(num1, num2)

    o = input('연산자 : ')
    result = c.exec(o)
    print('계산결과 : %d' % result)



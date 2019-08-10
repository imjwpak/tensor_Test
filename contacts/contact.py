class Contact:
    def __init__(self, n, p, e, a):
        self.n = n
        self.p = p
        self.e = e
        self.a = a

    def to_string(self):
        t = f'이름 : {self.n} \n전화번호 : {self.p} \n이메일 : {self.e} \n주소 : {self.a}'
        return t
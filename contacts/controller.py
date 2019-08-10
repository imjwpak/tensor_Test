from contacts.model import ContactsModel

class ContactsController:
    def __init__(self):
        self.model = ContactsModel()

    @staticmethod
    def print_menu():
        print('1. 연락처 입력')
        print('2. 연락처 츨력')
        print('3. 연락처 삭제')
        print('0. 종료')
        menu = int(input('메뉴 선택 : '))
        return menu

    def run(self):
        contacts = []

        while 1:
            menu = self.print_menu()
            print('메뉴 : %s' % menu)

            if menu == 1:
                n = input('이름 : ')
                p = input('전화번호 : ')
                e = input('이메일 : ')
                a = input('주소 : ')
                t = self.model.set_contact(n, p, e, a)
                contacts.append(t)
            elif menu == 2:
                print(self.model.get_contacts(contacts))
            elif menu == 3:
                n = input('삭제할 이름 : ')
                self.model.del_contact(contacts, n)
            elif menu == 0:
                print('시스템 종료')
                break
                

from contacts.contact import Contact

class ContactsModel:
    def __init__(self):
        pass

    # setter
    # 등록은 1개씩
    # self가 없으면 static 메서드
    # self가 있으면 instance 메서드
    @staticmethod
    def set_contact(n, p, e, a):
        contact = Contact(n, p, e, a)

        return contact

    # getter
    # 획득은 여러개 가능
    @staticmethod
    def get_contacts(params):
        contacts = []
        for i in params:
            contacts.append(i.to_string())
        return ''.join(contacts)

    @staticmethod
    def del_contact(params, n):
        for i, t in enumerate(params):
            if t.n == n:
                del params[i]

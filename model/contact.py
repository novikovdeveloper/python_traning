from sys import maxsize


class Contact:
    def __init__(self, firstname=None, middlename=None, lastname=None, nickname=None, title=None, company=None, address=None, home=None, mobile=None,
                        work=None, fax=None, email=None, email2=None, email3=None, homepage=None, byear=None, ayear=None, address2=None, phone2=None, notes=None, id=None,
                 all_phones_from_home_page=None, all_emails_from_home_page=None):
        self.firstname = firstname
        self.middlename = middlename
        self.lastname = lastname
        self.nickname = nickname
        self.title = title
        self.company = company
        self.address = address
        self.home = home
        self.mobile = mobile
        self.work = work
        self.fax = fax
        self.email = email
        self.email2 = email2
        self.email3 = email3
        self.homepage = homepage
        self.byear = byear
        self.ayear = ayear
        self.address2 = address2
        self.phone2 = phone2
        self.notes = notes
        self.all_phones_from_home_page = all_phones_from_home_page
        self.all_emails_from_home_page = all_emails_from_home_page
        self.id = id

    def __repr__(self):
        return "%s:%s:%s:%s:%s:%s:%s:%s:%s:%s" % (self.firstname, self.lastname, self.address, self.id, self.home,
                    self.work, self.mobile, self.email, self.email2, self.email3)

    def __eq__(self, other):
        return (self.id is None or other.id is None or self.id == other.id) and self.firstname == other.firstname\
               and self.lastname == other.lastname\
               and self.address == other.address, self.home == other.home_phone, self.work == other.work_phone,\
               self.mobile == other.mobile_phone, self.email == other.email1, self.email2 == other.email2,\
               self.email3 == other.email3

    def id_or_max(self):
        if self.id:
            return int(self.id)
        else:
            return maxsize
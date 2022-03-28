# -*- coding: utf-8 -*-
from model.contact import Contact
import random
import string


constant = [
    Contact(firstname="firstname1",
            middlename="middlename1",
            lastname="lastname1",
            nickname="nickname1",
            title="title1",
            company="company1",
            address="address1",
            home="home1",
            work="work1",
            mobile="mobile1",
            email="email1",
            email2="email21",
            email3="email31"),

    Contact(firstname="firstname2",
            middlename="middlename2",
            lastname="lastname2",
            nickname="nickname2",
            title="title2",
            company="company2",
            address="address2",
            home="home2",
            work="work2",
            mobile="mobile2",
            email="email2",
            email2="email22",
            email3="email32")
]


def random_string(prefix, maxlen):
    symbols = string.ascii_letters + string.digits
    return prefix + "".join([random.choice(symbols) for i in range(random.randrange(maxlen))])


testdata = [Contact(firstname="", middlename="", lastname="", nickname="", title="",
            company="", address="", home="", work="", mobile="",
            email="", email2="", email3="")] + [Contact(firstname=random_string("Alex", 5), middlename=random_string("Middle", 10), lastname=random_string("Bolduin", 5),
                                             nickname=random_string("vasua228", 10), title=random_string("no title", 5), company=random_string("roga i kopita", 10), address=
                             random_string("Moscow,Pushkina str. app 13", 20), home=random_string("123456",10), work=random_string("7891011",10), mobile=random_string("7891011",10),
            email=random_string("exam", 10), email2=random_string("exam2", 10), email3=random_string("exam2", 10))
    for i in range(5)
]

# -*- coding: utf-8 -*-
from model.contact import Contact
import random
import string
import pytest


def random_string(prefix, maxlen):
    symbols = string.ascii_letters + string.digits + string.punctuation + " " * 10
    return prefix + "".join([random.choice(symbols) for i in range(random.randrange(maxlen))])


testdata = [Contact(firstname="", middlename="", lastname="", nickname="", title="",
            company="", address="", home="", work="", mobile="",
            email="", email2="", email3="")] + [Contact(firstname=random_string("Alex", 5), middlename=random_string("Middle", 10), lastname=random_string("Bolduin", 5),
                                             nickname=random_string("vasua228", 10), title=random_string("no title", 5), company=random_string("roga i kopita", 10), address=
                             random_string("Moscow,Pushkina str. app 13", 20), home=random_string("123456",10), work=random_string("7891011",10), mobile=random_string("7891011",10),
            email=random_string("exam", 10), email2=random_string("exam2", 10), email3=random_string("exam2", 10))
    for i in range(5)
]


@pytest.mark.parametrize("contact", testdata, ids=[repr(x) for x in testdata])
def test_add_contact(app, contact):
    old_contacts = app.contact.get_contact_list()
    app.contact.create(contact)
    assert len(old_contacts) + 1 == app.contact.count()
    new_contacts = app.contact.get_contact_list()
    old_contacts.append(contact)
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)




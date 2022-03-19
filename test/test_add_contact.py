# -*- coding: utf-8 -*-
from model.contact import Contact


def test_add_contact(app):
    old_contacts = app.contact.get_contact_list()
    contact = Contact(firstname="Alex", middlename="Middle", lastname="Bolduin", nickname="vasua228", title="no title", company="roga i kopita", address=
                             "Moscow,Pushkina str. app 13", home="870007784433", mobile="880005553535", work="89998887766", fax="87779998888",
                               email="email@email.com", email2="none", email3="none2", homepage="www.yandex.ru", byear="1990", ayear="2010", address2="Secondary address",
                               phone2="8885554433", notes="nothing to ptint")
    app.contact.create(contact)
    assert len(old_contacts) + 1 == app.contact.count()
    new_contacts = app.contact.get_contact_list()
    old_contacts.append(contact)
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)


def test_add_contact_empty(app):
    old_contacts = app.contact.get_contact_list()
    contact = Contact(firstname="", middlename="", lastname="", nickname="", title="", company="", address=
                             "", home="", mobile="", work="", fax="",
                               email="", email2="", email3="", homepage="", address2="",
                               phone2="", notes="")
    app.contact.create(contact)
    assert len(old_contacts) + 1 == app.contact.count()
    new_contacts = app.contact.get_contact_list()
    old_contacts.append(contact)
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)



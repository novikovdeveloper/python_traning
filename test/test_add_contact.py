# -*- coding: utf-8 -*-
from model.contact import Contact


def test_add_contact(app):
    app.contact.create(Contact(firstname="Alex", middlename="Middle", lastname="Bolduin", nickname="vasua228", title="no title", company="roga i kopita", address=
                             "Moscow,Pushkina str. app 13", home_phone="870007784433", mobile_phone="880005553535", work_phone="89998887766", fax="87779998888",
                               email="email@email.com", email2="none", email3="none2", homepage="www.yandex.ru", byear="1990", ayear="2010", address2="Secondary address",
                               phone2="homeles", notes="nothing to ptint"))


def test_add_contact_empty(app):
    app.contact.create(Contact(firstname="", middlename="", lastname="", nickname="", title="", company="", address=
                             "", home_phone="", mobile_phone="", work_phone="", fax="",
                               email="", email2="", email3="", homepage="", byear="", ayear="", address2="",
                               phone2="", notes=""))




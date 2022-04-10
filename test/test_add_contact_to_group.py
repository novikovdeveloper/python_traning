# -*- coding: utf-8 -*-
from model.contact import Contact
from model.group import Group
from fixture.orm import ORMFixture
import random
import re

db1 = ORMFixture(host="127.0.0.1", name="addressbook", user="root", password="")


def test_add_contact_to_group(app, db):
    if len(db.get_contact_list()) == 0:
        app.contact.create(Contact(firstname="test"))
    if len(db.get_group_list()) == 0:
        app.group.create(Group(name="test"))
    contact = random.choice(db.get_contact_list())
    group = random.choice(db.get_group_list())
    db.remove_all_contacts_from_random_group(group.id)
    app.contact.add_contact_to_group(contact.id, group.id)
    assert clear(str(db1.get_contacts_in_group(Group(id=group.id)))) == clear(str(contact))


def clear(s):
    return re.sub("[\[\]]", "", s)
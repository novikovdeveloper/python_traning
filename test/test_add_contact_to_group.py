from model.contact import Contact
from model.group import Group


def test_add_first_contact_to_group(app, db, check_ui):
    if len(db.get_contact_list()) == 0:
        app.contact.create(Contact(firstname="test", middlename="test", lastname="test"))
    if len(db.get_group_list()) == 0:
        app.group.create(Group(name="Test_group", header="test_header", footer="test_footer"))
    old_contacts = db.get_contact_list()
    app.contact.add_first_contact_to_group()
    new_contacts = app.contact.get_contact_list()
    assert len(old_contacts) == len(new_contacts)
    if check_ui:
        assert sorted(new_contacts, key=Contact.id_or_max) == sorted(app.contact.get_contact_list(), key=Contact.id_or_max)



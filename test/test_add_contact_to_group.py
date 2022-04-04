from model.contact import Contact
from model.group import Group


def test_add_first_contact_to_group(app, db):
    if app.contact.count() == 0:
        app.contact.create(Contact(firstname="test", middlename="test", lastname="test"))
    if app.group.count() == 0:
        app.group.create(Group(name="Test_group", header="test_header", footer="test_footer"))
    app.contact.add_first_contact_to_group()



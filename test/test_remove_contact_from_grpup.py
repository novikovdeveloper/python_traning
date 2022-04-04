from model.contact import Contact
from model.group import Group


def test_remove_first_contact_from_group(app, db, check_ui):
    if len(db.get_contact_list()) == 0:
        app.contact.create(Contact(firstname="test", middlename="test", lastname="test"))
    if len(db.get_group_list()) == 0:
        app.group.create(Group(name="Test_group", header="test_header", footer="test_footer"))
    old_groups = db.get_group_list()
    app.contact.remove_first_contact_from_group()
    new_groups = db.get_group_list()
    assert len(old_groups) - 1 == len(new_groups)
    assert old_groups == new_groups
    if check_ui:
        assert sorted(new_groups, key=Group.id_or_max) == sorted(app.group.get_group_list(), key=Group.id_or_max)
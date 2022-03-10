from model.group import Group


def test_update_group(app):
    app.group.update_first_group(Group(name="Updated_name", header="Updated_header", footer="Updated_footer"))


def test_update_group_header(app):
    app.group.update_first_group(Group(header="New header"))

from model.group import Group


def test_update_group(app):
    app.session.login(username="admin", password="secret")
    app.group.update_group(Group(name="Updated_name", header="Updated_header", footer="Updated_footer"))
    app.session.logout()
from model.update_contact import UpdateFirstContact


def test_update_contact(app):
    app.session.login(username="admin", password="secret")
    app.update_contact.update_first_contact(UpdateFirstContact(firstname="Updated_Firstname", middlename="Updated_Middlename", lastname="Updated_Lastname", nickname="Updated_nickname"))
    app.session.logout()
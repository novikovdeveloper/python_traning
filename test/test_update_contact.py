from model.update_contact import UpdateFirstContact


def test_update_contact(app):
    app.update_contact.update_first_contact(UpdateFirstContact(firstname="Updated_Firstname", middlename="Updated_Middlename", lastname="Updated_Lastname", nickname="Updated_nickname"))

from model.update_contact import UpdateFirstContact
from model.contact import Contact


def test_update_contact(app):
    if app.contact.count() == 0:
        app.contact.create(Contact(firstname="", middlename="", lastname="", nickname="", title="", company="", address=
                             "", home_phone="", mobile_phone="", work_phone="", fax="",
                               email="", email2="", email3="", homepage="", byear="", ayear="", address2="",
                               phone2="", notes=""))
    app.update_contact.update_first_contact(UpdateFirstContact(firstname="Updated_Firstname", middlename="Updated_Middlename", lastname="Updated_Lastname", nickname="Updated_nickname"))

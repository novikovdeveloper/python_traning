from model.contact import Contact


def test_update_contact(app):
    if app.contact.count() == 0:
        app.contact.create(Contact(firstname="", middlename="", lastname="", nickname="", title="", company="", address=
                             "", home="", mobile="", work="", fax="",
                               email="", email2="", email3="", homepage="", address2="",
                               phone2="", notes=""))
    old_contacts = app.contact.get_contact_list()
    contact = Contact(firstname="Updated_Firstname", middlename="Updated_Middlename",
                            lastname="Updated_Lastname", nickname="Updated_nickname",
                            title="Updated_title", company="Updated_company", address=
                             "Updated_adress", home="Updated_phone", mobile="Updated_phone", work="Updated_workphone", fax="Updated_fax",
                            email="Updated_email", email2="Updated_email2", email3="Updated_email3", homepage="Updated_homepage", address2="Updated_adress2",
                            phone2="Updated_phone", notes="Updated_notes")
    contact.id = old_contacts[0].id
    app.contact.update_first_contact(contact)
    new_contacts = app.contact.get_contact_list()
    assert len(old_contacts) == len(new_contacts)


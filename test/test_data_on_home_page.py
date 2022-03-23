import re
from random import randrange


def test_some_data_on_contacts_page(app):
    data_on_contacts_page = app.contact.get_contact_list()
    index = randrange(len(data_on_contacts_page))
    identity_data_on_homepage = data_on_contacts_page[index]
    identity_data_on_edit_page = app.contact.get_contact_info_from_edit_page(index)
    assert identity_data_on_homepage.id == identity_data_on_edit_page.id
    assert identity_data_on_homepage.firstname == identity_data_on_edit_page.firstname
    assert identity_data_on_homepage.lastname == identity_data_on_edit_page.lastname
    assert identity_data_on_homepage.address == identity_data_on_edit_page.address
    assert identity_data_on_homepage.all_phones_from_home_page == merge_phones_like_on_home_page(identity_data_on_edit_page)
    assert identity_data_on_homepage.all_emails_from_home_page == merge_emails_like_on_home_page(identity_data_on_edit_page)


#очищаем недопустимые смволы с помощью регулярных выражений
def clear(s):
    return re.sub("[() -]", "", s)


def merge_phones_like_on_home_page(contact):
    return "\n".join(filter(lambda x: x != "",
                            map(lambda x: clear(x),
                                filter(lambda x: x is not None,
                                       [contact.home, contact.work, contact.mobile, contact.phone2]))))


def merge_emails_like_on_home_page(contact):
    return "\n".join(filter(lambda x: x != "",
                            filter(lambda x: x is not None,
                                   [contact.email, contact.email2, contact.email3])))

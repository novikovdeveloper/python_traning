from model.contact import Contact


class ContactHelper:
    def __init__(self, app):
        self.app = app

    def create(self, contact):
        wd = self.app.wd
        self.open_add_new()
        self.fill_contact_form(contact)
        wd.find_element_by_xpath("//div[@id='content']/form/input[21]").click()

    def open_add_new(self):
        wd = self.app.wd
        if not (wd.current_url.endswith("/edit.php") and len(wd.find_elements_by_name("submit")) > 0):
            wd.find_element_by_link_text("add new").click()

    def fill_contact_form(self, contact):
        wd = self.app.wd
        self.change_field_name("firstname", contact.firstname)
        self.change_field_name("middlename", contact.middlename)
        self.change_field_name("lastname", contact.lastname)
        self.change_field_name("nickname", contact.nickname)
        self.change_field_name("title", contact.title)
        self.change_field_name("company", contact.company)
        self.change_field_name("address", contact.address)
        self.change_field_name("home", contact.home)
        self.change_field_name("mobile", contact.mobile)
        self.change_field_name("work", contact.work)
        self.change_field_name("fax", contact.fax)
        self.change_field_name("email", contact.email)
        self.change_field_name("email2", contact.email2)
        self.change_field_name("email3", contact.email3)
        self.change_field_name("homepage", contact.homepage)
        self.change_field_name("address2", contact.address2)
        self.change_field_name("phone2", contact.phone2)
        self.change_field_name("notes", contact.notes)

    def change_field_name(self, field_name, text):
        wd = self.app.wd
        if text is not None:
            wd.find_element_by_name(field_name).click()
            wd.find_element_by_name(field_name).clear()
            wd.find_element_by_name(field_name).send_keys(text)

    def delete_first_contact(self):
        wd = self.app.wd
        self.open_contacts_page()
        self.select_first_contact()
        wd.find_element_by_xpath("//input[@value='Delete']").click()
        wd.switch_to.alert.accept()
        self.open_contacts_page()

    def select_first_contact(self):
        wd = self.app.wd
        wd.find_element_by_name("selected[]").click()

    def update_first_contact(self, new_contact_data):
        wd = self.app.wd
        self.open_contacts_page()
        self.select_first_contact()
        wd.find_element_by_xpath("//img[@alt='Edit']").click()
        self.fill_contact_form(new_contact_data)
        wd.find_element_by_name("update").click()
        self.open_contacts_page()

    def open_contacts_page(self):
        wd = self.app.wd
        if not wd.current_url.endswith("/addressbook/"):
            wd.find_element_by_link_text("home").click()

    def return_to_homepage(self):
        wd = self.app.wd
        wd.find_element_by_link_text("home page").click()

    def count(self):
        wd = self.app.wd
        self.open_contacts_page()
        return len(wd.find_elements_by_name("selected[]"))

    def get_contact_list(self):
        wd = self.app.wd
        self.app.open_home_page()
        #self.open_contacts_page()
        contacts = []
        rows = wd.find_elements_by_xpath("/html/body/div/div[4]/form[2]/table/tbody/tr[@name='entry']")
        for elements in rows:
            column = elements.find_elements_by_tag_name("td")
            firstname = column[2].text
            lastname = column[1].text
            id = elements.find_element_by_name("selected[]").get_attribute("value")
            contacts.append(Contact(lastname=lastname, firstname=firstname, id=id))
        return contacts

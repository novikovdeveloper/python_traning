# -*- coding: utf-8 -*-         указываем кодировку обязательно, если испоьльзуем кирилицу
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest
from group import Group


class test_add_group(unittest.TestCase):
    def setUp(self):
        self.wd = webdriver.Firefox()

    def test_add_group(self):
        wd = self.wd
        self.open_home_page(wd)   # приозвели рефакторинг по нескольким действиям extract method
        self.login(wd, username="admin", password="secret") #указали имя и пароль
        self.open_groups_page(wd)
        self.create_group(wd, Group(name="test", header="test", footer="test")) #заключили параметры в метод Group
        self.return_to_groups_page(wd)
        self.logout(wd)

    def test_add_empty_group(self): #второй тестовый метод с пустыми значениями проверок
        wd = self.wd
        self.open_home_page(wd)   # приозвели рефакторинг по нескольким действиям extract method
        self.login(wd, username="admin", password="secret") #указали имя и пароль
        self.open_groups_page(wd)
        self.create_group(wd, Group(name="", header="", footer=""))  #заключили параметры в метод Group
        self.return_to_groups_page(wd)
        self.logout(wd)

    def logout(self, wd):
        wd.find_element_by_link_text("Logout").click()

    def return_to_groups_page(self, wd):
        wd.find_element_by_link_text("group page").click()

    def create_group(self, wd, group):  #тоже убрали зн-я по умолчанию и добавили передачу параметров в файл group
        # init group creatinon
        wd.find_element_by_name("new").click()
        # fill group form
        wd.find_element_by_name("group_name").click()
        wd.find_element_by_name("group_name").clear()
        wd.find_element_by_name("group_name").send_keys("%s" % group.name)
        wd.find_element_by_name("group_header").click()
        wd.find_element_by_name("group_header").clear()
        wd.find_element_by_name("group_header").send_keys(group.header)
        wd.find_element_by_name("group_footer").click()
        wd.find_element_by_name("group_footer").clear()
        wd.find_element_by_name("group_footer").send_keys("%s" % group.footer)
        # submit group creation
        wd.find_element_by_name("submit").click()

    def open_groups_page(self, wd):
        wd.find_element_by_link_text("groups").click()

    def login(self, wd, username, password):  #рефакторинг через changes signature для изменения дефолтных значений username и passwoed по умолчанию
        wd.find_element_by_name("user").click()
        wd.find_element_by_name("user").clear()
        wd.find_element_by_name("user").send_keys("%s" % username) #рефакторинг через introduсe parameter (username и password)
        wd.find_element_by_name("pass").click()
        wd.find_element_by_name("pass").clear()
        wd.find_element_by_name("pass").send_keys("%s" % password)
        wd.find_element_by_xpath("//input[@value='Login']").click()

    def open_home_page(self, wd):
        wd.get("http://localhost/addressbook/")

    def is_element_present(self, how, what):
        try: self.wd.find_element(by=how, value=what)
        except NoSuchElementException as e: return False
        return True
    
    def is_alert_present(self):
        try: self.wd.switch_to_alert()
        except NoAlertPresentException as e: return False
        return True

    def tearDown(self):
        self.wd.quit()


if __name__ == "__main__":
    unittest.main()

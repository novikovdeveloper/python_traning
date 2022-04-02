# создан файл для связи с БД и извлечения данных из нее
from fixture.db import DbFixture

db = DbFixture(host="127.0.0.1", name="addressbook", user="root", password="")

# извлечем информацию из таблицы group_list в виде набора строк
try:
    contacts = db.get_contact_list()
    for contact in contacts:
        print(contact)
    print(len(contacts))
finally:
    db.destroy()
# создан файл для связи с БД и извлечения данных из нее
from fixture.orm import ORMFixture
from model.group import Group

db = ORMFixture(host="127.0.0.1", name="addressbook", user="root", password="")

# извлечем информацию из таблицы в виде набора строк
try:
    l = db.get_contacts_not_in_group(Group(id="138"))
    for item in l:
        print(item)
    print(len(l))
finally:
    pass #db.destroy()
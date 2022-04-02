# создан файл для связи с БД и извлечения данных из нее
from fixture.orm import ORMFixture

db = ORMFixture(host="127.0.0.1", name="addressbook", user="root", password="")

# извлечем информацию из таблицы group_list в виде набора строк
try:
    l = db.get_contact_list()
    for item in l:
        print(item)
    print(len(l))
finally:
    pass #db.destroy()
# создан файл для связи с БД и извлечения данных из нее
import pymysql.cursors

connection = pymysql.connect(host="127.0.0.1", database="addressbook", user="root", password="")

# извлечем информацию из таблицы group_list в виде набора строк
try:
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM group_list")
    for row in cursor.fetchall():
        print(row)
finally:
    connection.close()
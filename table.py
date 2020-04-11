# # Импорт библиотеки
# import sqlite3
#
#
# '''Удаление таблицы'''
# conn = sqlite3.connect("db.sqlite3")
# cursor = conn.cursor()
#
# cursor.execute('drop table blog_tag')
# conn.commit()
# cursor.close()
# conn.close()

import sqlite3 as lite
import sys

con = lite.connect('db.sqlite3')

with con:
    cur = con.cursor()
    cur.execute("SELECT * FROM blog_category")
    rows = cur.fetchall()

    for row in rows:
        print(row)
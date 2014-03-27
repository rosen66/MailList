import sqlite3

def create_table_users(cursor):
    cursor.execute('''CREATE TABLE users(id INTEGER PRIMARY KEY ASC, name Text)''')

def create_table_mails(cursor):
    cursor.execute('''CREATE TABLE mail(id INTEGER PRIMARY KEY ASC, mail Text)''')

def create_table_join_table(cursor):
    cursor.execute('''CREATE TABLE join_table(user_id int, mail_id int
        FOREIGN KEY(user_id) REFERENCES users(id)
        FOREIGN KEY(trackartist) REFERENCES mail(id))''')

conn = sqlite3.connect("dataBase.db")

cT1 = conn.cursor()
create_table_users(cT1)
conn.commit()

cT2 = conn.cursor()
create_table_mails(cT1)
conn.commit()

cT3 = conn.cursor()
create_table_join_table(cT1)
conn.commit()

conn.close()

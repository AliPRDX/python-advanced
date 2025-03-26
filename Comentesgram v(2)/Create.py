import sqlite3


def create():
    conn = sqlite3.connect("Login.db")
    cur = conn.cursor()
    cur.execute("CREATE TABLE Current_user_login (user,pass,role);")
    print("Successfully created table accounts")
    conn.commit()
    conn.close()


# def insert():
#     conn = sqlite3.connect("Login.db")
#     cur = conn.cursor()
#     cur.execute("INSERT INTO accounts VALUES ('Ali','Ali123','User');")
#     print("Successfully inserted record")
#     conn.commit()
#     conn.close()
#
#
# def select():
#     conn = sqlite3.connect("Login.db")
#     cur = conn.cursor()
#     cur.execute("SELECT * FROM accounts;")
#     records = cur.fetchall()
#     for i in records:
#         print(i[0])
#     conn.commit()
#     conn.close()


create()
# insert()
# select()

import sqlite3


class Database:
    def __init__(self):
        pass

    def create_table(self):
        db_name = input("Enter Database Name: ")
        conn = sqlite3.connect(f"{db_name}.db")
        cur = conn.cursor()
        t_name = input("Enter table name: ")
        t_num_records = int(input("How many records do you want? : "))
        record = []
        record2 = []
        for i in range(t_num_records):
            t_records = input("Enter table records: ")
            record2.append(t_records)
            t_type_records = input("Enter record type type:(TEXT, INTEGER) ").upper()
            record.append(f"{t_records} {t_type_records}")
        record_query = ", ".join(record)

        cur.execute(f"CREATE TABLE IF NOT EXISTS {t_name} ({record_query});")
        print(f"Successfully created table {t_name}")
        conn.commit()
        conn.close()
        self.insert_data()

    def insert_data(self):
        db_name = input("Enter Database Name: ")
        t_name = input("Enter table name to insert data : ")
        value = []
        conn = sqlite3.connect(f"{db_name}.db")
        cur = conn.cursor()
        cur.execute(f"PRAGMA table_info({t_name})")
        columns = [col[1] for col in cur.fetchall()]
        n = 0
        for i in columns:
            t_r_value = input(f"Enter record {columns[n]} value: ")
            value.append(t_r_value)
            n += 1
        value_query = ", ".join(["?"] * len(columns))
        cur.execute(f"INSERT INTO {t_name} VALUES ({value_query})", value)
        print(f"Successfully inserted records")
        conn.commit()
        conn.close()

    def show_data(self):
        db_name = input("Enter Database Name: ")
        t_name = input("Enter table name to insert data : ")
        conn = sqlite3.connect(f"{db_name}.db")
        cur = conn.cursor()
        cur.execute(f"PRAGMA table_info({t_name})")
        columns = [col[1] for col in cur.fetchall()]
        print(columns)
        cur.execute(f"SELECT * FROM {t_name} ;")
        records = cur.fetchall()
        for i in records:
            print(i)
        conn.commit()

        choose = input("Do you want to filter the database?(Y/N):").lower()
        if choose == "y":
            filter_column = input("Enter filter column: ")
            filter_operator = input("Enter filter operator (>, <, =, >=, <=): ")
            filter_value = input("Enter filter value: ")
            cur.execute(f"SELECT * FROM {t_name} WHERE {filter_column} {filter_operator} ?", (filter_value,))
            records = cur.fetchall()
            for i in records:
                print(i)
            conn.commit()
        elif choose == "n":
            pass
        else:
            print("Please enter Y or N")
            self.show_data()
        conn.close()


def menu():
    db = Database()
    while True:
        choice = input("1. Create Table\n2. Insert Data\n3. Show Data\n4. Exit\nChoose: ")
        if choice == "1":
            db.create_table()
        elif choice == "2":
            db.insert_data()
        elif choice == "3":
            db.show_data()
        elif choice == "4":
            break
        else:
            print(" Invalid choice! Try again.")


menu()

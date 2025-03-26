import subprocess
import sqlite3
import re


class Usermanager:
    def __init__(self):
        self.usernames = []
        self.passwords = []
        self.roles = []
        self.email = []

    def read_users(self):
        conn = sqlite3.connect("Login.db")
        cur = conn.cursor()
        cur.execute("SELECT * FROM accounts;")
        records = cur.fetchall()
        for i in records:
            self.usernames.append(i[0])
            self.passwords.append(i[1])
            self.roles.append(i[2])
            self.email.append(i[3])

    def Current_user_login(self):
        conn = sqlite3.connect("Login.db")
        cur = conn.cursor()
        cur.execute("Delete FROM Current_user_login;")
        conn.commit()
        conn = sqlite3.connect("Login.db")
        conn.close()

    def login(self):
        self.read_users()
        username = input("Enter your username or email: ").lower()
        password = input("Enter your password: ")
        if username in self.usernames or username in self.email:
            if username in self.usernames:
                index = self.usernames.index(username)
                username = self.usernames[index]
            if username in self.email:
                index = self.email.index(username)
                username = self.usernames[index]
            if self.passwords[index] == password:
                print("Welcome " + username + "!")
                role = self.roles[index]
                self.Current_user_login()
                conn = sqlite3.connect("Login.db")
                cur = conn.cursor()
                cur.execute("INSERT INTO Current_user_login VALUES (?, ?, ?)", (username, password, role))
                conn.commit()
                conn.close()
                subprocess.run(['python', 'Comentesgram.py'])
            else:
                print("Wrong username or password!")

        else:
            print("Wrong username or password!")

    def signup(self):
        self.read_users()
        email = input("Enter your email address: ").lower()
        username = input("Enter your username: ").lower()
        password = input("Enter your password: ")
        if 5 <= len(username) <= 16:
            if username not in self.usernames:
                if 8 <= len(password) <= 16 and re.search("[A-Z]", password) and re.search("[0-9]", password):
                    self.save_user(username, password, email)
                else:
                    print(
                        "The password must be between 8 and 16 characters long and contain at least one uppercase letter and at least one number.")
            else:
                print("Username already exists!")
        else:
            print("Username length must be between 5 and 16 characters!")

    def save_user(self, username, password, email):
        conn = sqlite3.connect("Login.db")
        cur = conn.cursor()
        cur.execute("INSERT INTO accounts VALUES (?, ?, ?,?)", (username, password, "user", email))
        conn.commit()
        print("Sign up successful")
        conn.close()

    def menu(self):
        while True:
            choice = input("\nDo you want to sign up or login? (1=Sign Up, 2=Login, 3=Exit): ")
            if choice == "1":
                self.signup()
            elif choice == "2":
                self.login()
            elif choice == "3":
                print("exiting ...")
                exit()
            else:
                print("Invalid choice! Please enter 1, 2, or 3")


start = Usermanager()
start.menu()

import jdatetime
import sqlite3


class Comment:

    def __init__(self, username, password):
        self.username = username
        self.password = password

    def user_menu(self):
        while True:
            choice = input("\n1. Leave a comment\n2. Like & Dislike.\n3. Show comments.\n4. Log out\nSelect: ")
            if choice == "1":
                self.like_comment()
            elif choice == "2":
                self.Leave_comment()
            elif choice == "3":
                self.show_comments()
            elif choice == "4":
                print("Logging out...")
                break
            else:
                print("Invalid input")

    def Leave_comment(self):
        comment = input("Leave a comment: ")
        if comment == "":
            print("Comment cannot be empty.")
            self.Leave_comment()
        data = jdatetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        conn = sqlite3.connect("Login.db")
        cur = conn.cursor()
        cur.execute("INSERT INTO Comments VALUES (NULL,?,?,?,?,?)", (self.username, comment, 0, 0, data))
        conn.commit()
        print("Your comment has been successfully recorded.")
        conn.close()

    def show_comments(self):
        conn = sqlite3.connect("Login.db")
        cur = conn.cursor()
        cur.execute("SELECT * FROM Comments;")
        data = cur.fetchall()
        if not data:
            print("No comments available.")
        else:
            for comment in data:
                print(
                    f"ID: {comment[0]} | User: {comment[1]} | Comment: {comment[2]} | Like:{comment[3]} | Dislike:{comment[4]} | Date: {comment[5]} ")

    def like_comment(self):
        conn = sqlite3.connect("Login.db")
        cur = conn.cursor()
        cur.execute("SELECT * FROM Comments;")
        data = cur.fetchall()

        self.show_comments()
        choice = input("Would you like to like or dislike a comment? (1=Like, 2=Dislike, 3=Exit): ")
        id = int(input("Enter a comment ID: "))
        if choice == "1":
            for comment in data:

                if comment[0] == id:
                    like = comment[3]
                    like += 1
                    cur.execute("UPDATE Comments SET Like = ? WHERE ID = ?", (like, id))
                    conn.commit()
                    print("The comment you wanted was liked.")


        elif choice == "2":
            for comment in data:
                if comment[0] == id:
                    dislike = comment[3]
                    dislike += 1
                    cur.execute("UPDATE Comments SET Like = ? WHERE ID = ?", (dislike, id))
                    conn.commit()
            print("The comment you wanted was disliked.")
        elif choice == "3":
            self.user_menu()
        else:
            print("Invalid input")

        conn.close()


class Admin(Comment):
    def __init__(self, username, password):
        super().__init__(username, password)

    def admin_menu(self):
        while True:
            choice = input("\n1. Show comments\n2. Delete comments.\n3.Leave a comment \n4.Like & Dislike \n5.Log out "
                           "\nSelect: ")
            if choice == "1":
                self.show_comments()
            elif choice == "2":
                self.delete_comment()
            elif choice == "3":
                self.Leave_comment()
            elif choice == "4":
                self.like_comment()
            elif choice == "5":
                print("Logging out...")
                break
            else:
                print("Invalid selection")

    def delete_comment(self):
        conn = sqlite3.connect("Login.db")
        cur = conn.cursor()
        cur.execute("SELECT * FROM Comments;")
        data = cur.fetchall()
        self.show_comments()
        try:

            del_id = int(input("Which ID do you want to delete?"))
            for comment in data:
                if comment[0] == del_id:
                    print(
                        f"ID: {comment[0]} | User: {comment[1]} | Comment: {comment[2]} | Like:{comment[3]} | Dislike:{comment[4]} | Date: {comment[5]} ")

                    confirm = input("Are you sure you want to delete this comment? (y/n): ").lower()
                    if confirm == "y":
                        cur.execute("Delete FROM Comments WHERE ID = ?", (del_id,))
                        conn.commit()
                        conn.close()
                        print("Comment deleted.")
                        return
                    else:
                        print("Deletion canceled.")
                        return

            print("ID not found!")


        except ValueError:
            print("Invalid input! Please enter a valid ID.")


def login_user():
    conn = sqlite3.connect("Login.db")
    cur = conn.cursor()
    cur.execute("SELECT * FROM Current_user_login;")
    user = cur.fetchall()
    for i in user:
        username = i[0]
        password = i[1]
        role = i[2]
    user_start = Comment(username, password)
    admin_start = Admin(username, password)
    if role != "Admin":
        user_start.user_menu()
    else:
        admin_start.admin_menu()


login_user()

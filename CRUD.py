# Login -> Interface -> exit/delete/edit/post/like? -> edit screen/post screen -> back/post
import os
import sqlite3

size = os.get_terminal_size()
print(f"Columns: {size.columns}, Lines: {size.lines}")
login = True
Login_dict = {"admin": "12345$"}
post_dict = {}

def Login_screen():
    global Id
    print("\nHi! Welcome to this simple CRUD app! \nIf you must, type 'exit' to exit.\n")
    Id = input("What is your ID? If it is your first time here, type 'register' to register for an account. Enter here: ")
    ID_and_passcode()

def center_text(text):
    total_length = size.columns
    text_length = len(text)
    if text_length >= total_length:
        return text
    padding = ((total_length - text_length) // 2) -1
    return "-" * padding + " "+ text+ " " + "-" * padding

def register():
    print(center_text("Registering Interface"))
    while True:
        registerid = input("What do you want to be called (this is your ID): ")
        if registerid.lower() == "exit":
            print("See you next time!")
            return
        elif registerid in Login_dict:
            print("Sorry, that ID is in use.")
        else:
            break
    while True:
        registerpasswd = input("What do you want your password to be? ")
        if registerpasswd.lower() == "exit":
            print("See you next time!")
            return
        else:
            Login_dict[registerid] = registerpasswd
            print("\nAccount successfully created!")
            return

def Enter_Interface():
    global login
    print(center_text("Interface"))

    no_exit = True
    while no_exit:
        user_top_posts = post_dict[Id] if Id in post_dict else "You have no posts yet."
        choice = input("What do you want to do? (Options: delete, edit, post, view, logout): ")
        print(f"You can type 'logout' to logout at any time.\n")
        print(user_top_posts)

        if choice == "logout":
            print("See you next time!")
            login = True
            no_exit = False

        elif choice == "edit":
            print("Edit selected (not implemented yet).")

        elif choice == "post":
            print("What do you want to post?")

        elif choice == "delete":
            print("Delete selected (not implemented yet).")

        elif choice == "view":
            print("Like selected (not implemented yet).")

        else:
            print("Invalid option.")

class post:
    def __init__(self, poster, password, post, likes):
        self.poster = poster
        self.likes = likes
        self.post = post
        self.password = password

    def __repr__(self):
        return f"This is a post by {self.poster}, likes: {self.likes}, with content: {self.post}"
    
    def add_post(self):
        conn = sqlite3.connect("Crud.db")
        c = conn.cursor()
        c.execute(f"""INSERT INTO "Crud Storage" (UserID, password, post, likes) VALUES ('{self.poster}', '{self.password}', '{self.post}', '0');""")
        conn.commit()
        conn.close()

    def welcome_message(self):
        conn = sqlite3.connect("Crud.db")
        c = conn.cursor()
        c.execute(f"""INSERT INTO "Crud Storage" (UserID, password, post, likes) VALUES ('{self.poster}', '{self.password}', 'Welcome {self.poster}.', '0');""")
        conn.commit()
        conn.close()

def ID_and_passcode():
    global login

    if Id.lower() == "exit":
        print("See you next time!")
        login = False

    elif Id.lower() == "register":
        register()

    elif Id in Login_dict:
        print("You have entered a valid ID.")
        Password = input("Please enter your passcode here, or type back to go back: ")

        if Password.lower() == "back":
            print("")

        elif Password == Login_dict[Id]:
            print("Correct Password Entered.\n")
            Enter_Interface()

        else:
            print("Wrong password entered. Please try again.")

    else:
        print("Invalid ID entered.")

while login:
    Login_screen()

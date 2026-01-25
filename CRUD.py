# Login -> Interface -> exit/delete/edit/post/like? -> edit screen/post screen -> back/post
import os
size = os.get_terminal_size()
print(f"Columns: {size.columns}, Lines: {size.lines}")
login = True
Login_dict = {"admin": "12345$"}

def Login_screen():
    global Id
    print("Hi! Welcome to this simple CRUD app! If you must, type 'exit' to exit.")
    Id = input("What is your ID? If it is your first time here, type 'register' to register for an account. Enter here: ")
    ID_and_passcode()

def register():
    print(((((size.columns-21)//2)-2)*"-")+"Registering Interface"+(((size.columns-21)//2)-2)*"-")
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
            print("Account successfully created!\n\n")
            return

def Enter_Interface():
    global login
    print(f"-Interface-")
    print(f"You can type 'logout' to logout at any time.\n")

    no_exit = True
    while no_exit:
        choice = input("What do you want to do? (Options: delete, edit, post, like, logout): ")

        if choice == "logout":
            print("See you next time!")
            login = True
            no_exit = False

        elif choice == "edit":
            print("Edit selected (not implemented yet).")

        elif choice == "post":
            print("Post selected (not implemented yet).")

        elif choice == "delete":
            print("Delete selected (not implemented yet).")

        elif choice == "like":
            print("Like selected (not implemented yet).")

        else:
            print("Invalid option.")

class post:
    def __init__(self, poster, unique_id, likes):
        self.poster = poster
        self.unique_id = unique_id
        self.likes = likes

    def __repr__(self):
        return f"This is a post by {self.poster}, post ID {self.unique_id}, likes: {self.likes}"

def ID_and_passcode():
    global login

    if Id.lower() == "exit":
        print("See you next time!")
        login = False

    elif Id.lower() == "register":
        register()

    elif Id in Login_dict:
        print("You have entered a valid ID.")
        Password = input("Please enter your passcode here, or type exit to exit: ")

        if Password.lower() == "exit":
            print("See you next time!")
            login = False

        elif Password == Login_dict[Id]:
            print("Correct Password Entered.\n")
            login = False
            Enter_Interface()

        else:
            print("Wrong password entered. Please try again.")

    else:
        print("Invalid ID entered.")

while login:
    Login_screen()

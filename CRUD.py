# Login -> Interface -> exit/delete/edit/post/like? -> edit screen/post screen -> back/post

accessing_app = True
Login_dict= {"admin": "12345$"}
def main():
    global Id
    print("Hi! Welcome to this simple CRUD app! If you must, type 'exit' to exit.")
    Id = str(input("What is your ID? If it is your first time here, type 'register' to register for an account. Enter here: "))
    ID_and_passcode()

def register():
    print("     -----Registering Interface-----     \n If need be, type 'exit' to exit.")
    registerid = str(input("What do you want to be called (this is your ID): "))
    if registerid.lower() == "exit":
        print("\nSee you next time!")
    elif registerid in Login_dict:
        print("\nSorry, that ID is in use.")
        register()
    else:
        registerpasswd = str(input("What do you want your password to be? "))
        if registerpasswd.lower() == "exit":
            print("\nSee you next time!")
        else:
            Login_dict[registerid] = registerpasswd

def Enter_Interface():
    pass
class post:
    def __init__(self, poster, unique_id, likes):
        self.poster = poster
        self.unique_id = unique_id
        self.likes = likes
    def __repr__(self):
        print(f"This is a post by a user named {self.poster}, the post ID is {self.unique_id}, and has {self.likes}")

def ID_and_passcode():
    global accessing_app
    if Id.lower() == "exit":
        print("See you next time!")
        accessing_app = False    
    elif Id.lower() == "register":
        register()
    elif Id in Login_dict:
        print("You have entered a valid Id.")
        Password = input("Please enter your passcode here, or type exit to exit: ")
        if Password == "exit":
            print("See you next time!")
            accessing_app = False    
        elif Password == Login_dict[Id]:
            print("Correct Password Entered.")
            Enter_Interface()
        else:
            print("Wrong password entered. Please try again.")
    else:
        print("Invalid ID entered.")

while accessing_app == True:
    main()
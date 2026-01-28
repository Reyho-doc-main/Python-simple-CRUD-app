import os
from crud import verify_user, create_user, create_post, read_posts, update_post, delete_post, like_post, read_own_posts
size = os.get_terminal_size()
current_user_id = None
app_running = True
def center_text(text):
    total_length = size.columns
    text_length = len(text)
    if text_length >= total_length:
        return text
    padding = ((total_length - text_length) // 4) -1
    return "- " * padding + " "+ text+ " " + " -" * padding

def login():
    global current_user_id, app_running
    print("\n" + center_text("Login"))
    print("\nHi! Welcome to this simple CRUD app! \nIf you must, type 'exit' to exit.\n")
    id_input = input("What is your ID? If it is your first time here, type 'register' to register for an account. Enter here: ")
    if id_input.lower() == "register":
        register()
    elif id_input.lower() == "exit":
        print("See you next time!")
        app_running = False
        return
    else:
        password_input = input("Enter your password: ")
        user_id = verify_user(id_input, password_input)
        if password_input.lower() == "exit":
            print("See you next time!")
            app_running = False
            return
        elif user_id is None:
            print("Invalid credentials.")
            return
        else:
            current_user_id = user_id
            interface()


def register():
    print(center_text("Registering Interface"))
    print("To exit registration, type 'back' at any prompt.\n")
    while True:
        username = input("What do you want to be called (this is your ID): ")
        if username.lower() == "back":
            return
        password = input("What do you want your password to be? ")
        if password.lower() == "back":
            return
        success = create_user(username, password)
        if success:
            print("Registration successful! You can now log in.")
            return
        else:
            print("Registration failed. Username may already be taken. Try again.")


def interface():
    global current_user_id

    while True:
        print("\nOptions: post, view, edit, delete, logout")
        choice = input("> ")
        if choice == "logout":
            current_user_id = None
            break

        elif choice == "post":
            post = input("What do you want to post? (type back to go back): ")
            if post.lower() == "back":
                continue
            else:
                create_post(current_user_id, post)

        elif choice == "view":
            posts = read_posts()
            print("\n" + "Posts")
            for post in posts:
                print(f"Post ID: {post[0]} | Likes: {post[3]}")
                print(f"Content: {post[2]}\n")
            like = input("Type the Post ID to like a post, or 'back' to go back: ")
            if like.lower() == "back":
                continue
            else:
                if like.isdigit():
                    post_id = int(like)
                    liked = like_post(post_id, current_user_id)
                    if liked:
                        print("Post liked!")
                    else:
                        print("You have already liked this post or it does not exist.")

        elif choice == "edit":
            view_own_post()
            post_id_input = input("Enter the Post ID of the post you want to edit (or type 'back' to go back): ")
            if post_id_input.lower() == "back":
                continue
            else:
                if post_id_input.isdigit():
                    post_id = int(post_id_input)
                    new_content = input("Enter the new content for your post: ")
                    updated = update_post(post_id, new_content, current_user_id)
                    if updated:
                        print("Post updated successfully.")
                    else:
                        print("Failed to update post. Make sure the Post ID is correct.")

        elif choice == "delete":
            view_own_post()
            pid = input("Post ID to delete: ")
            if pid.isdigit():
                if delete_post(int(pid), current_user_id):
                    print("Post deleted.")
                else:
                    print("Failed to delete post.")
        else:
            print("Invalid option.")

def view_own_post():
    global current_user_id
    posts = read_own_posts(current_user_id)
    print("\n" + "Your Posts")
    for post in posts:
        print(f"Post ID: {post[0]} | User ID: {post[1]} | Likes: {post[3]}")
        print(f"Content: {post[2]}\n")


while app_running == True:
    login()
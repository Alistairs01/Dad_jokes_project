from models.users import Users
from models.jokes import Jokes

def exit_program():
    print("Bye!")
    exit()

def find_user_by_name():
    name = input("Enter user name: ")
    user = Users.find_by_username(name)
    print(f'User: {user}' if user else "User not found")

def find_user_by_id():
    try:
        id_ = int(input("Enter user id: "))
        user = Users.find_by_id(id_)
        print(f'User: {user}' if user else "User not found")
    except ValueError:
        print("Invalid input. Please enter a valid user id.")

def create_user():
    name = input("Enter user name: ")
    email = input("Enter user email: ")
    try:
        user = Users.create(name, email)
        print(f'User created: {user}')
    except Exception as e:
        print(f'User not created: {e}')

def update_user():
    try:
        id_ = int(input("Enter user id: "))
        user = Users.find_by_id(id_)
        if user:
            try:
                name = input("Enter user name: ")
                email = input("Enter user email: ")
                user.name = name
                user.email = email
                user.update()
                print(f'User updated: {user}')
            except Exception as e:
                print(f'User not updated: {e}')
        else:
            print("User not found")
    except ValueError:
        print("Invalid input. Please enter a valid user id.")

def delete_user():
    try:
        id_ = int(input("Enter user id: "))
        user = Users.find_by_id(id_)
        if user:
            user.delete()
            print(f'User deleted: {user}')
        else:
            print("User not found")
    except ValueError:
        print("Invalid input. Please enter a valid user id.")

def list_users():
    users = Users.get_all()
    for user in users:
        print(user)

def list_jokes():
    jokes = Jokes.get_all()
    for joke in jokes:
        print(joke)

def find_joke_by_id():
    try:
        id_ = int(input("Enter joke id: "))
        joke = Jokes.find_by_id(id_)
        print(f'Joke: {joke}' if joke else "Joke not found")
    except ValueError:
        print("Invalid input. Please enter a valid joke id.")

def find_joke_by_joke():
    joke_text = input("Enter joke: ")
    joke = Jokes.find_by_joke(joke_text)
    print(f'Joke: {joke}' if joke else "Joke not found")

def create_joke():
    try:
        user_id = int(input("Enter user id: "))
        joke_text = input("Enter joke: ").strip()

        # Validate user ID
        user = Users.find_by_id(user_id)
        if not user:
            print("Invalid user id.")
            return

        # Validate joke text
        if not joke_text:
            print("Joke must be a non-empty string.")
            return

        try:
            joke = Jokes.create(user_id, joke_text)
            print(f'Joke created: {joke}')
        except Exception as e:
            print(f'Joke not created: {e}')
    except ValueError:
        print("Invalid input. Please enter a valid user id.")
def update_joke():
    try:
        id_ = int(input("Enter joke id: "))
        joke = Jokes.find_by_id(id_)
        if joke:
            try:
                user_id = int(input("Enter user id: "))
                joke.user_id = user_id
                joke.update()
                print(f'Joke updated: {joke}')
            except Exception as e:
                print(f'Joke not updated: {e}')
        else:
            print("Joke not found")
    except ValueError:
        print("Invalid input. Please enter a valid joke id.")

def delete_joke():
    try:
        id_ = int(input("Enter joke id: "))
        joke = Jokes.find_by_id(id_)
        if joke:
            joke.delete()
            print(f'Joke deleted: {joke}')
        else:
            print("Joke not found")
    except ValueError:
        print("Invalid input. Please enter a valid joke id.")
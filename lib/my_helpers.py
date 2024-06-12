from models.users import Users
from models.jokes import Jokes

def exit_program():
    print("Bye!")
    exit()

def find_user_by_name():
    name = input("Enter user name: ")
    user = Users.find_by_username(name)
    print(f'User: {user}') if user else print ("User not found")
def find_user_by_id():
    id_ = int(input("Enter user id: "))
    user = Users.find_by_id(id_)
    print(user) if user else print ("User not found")
def create_user():
    name = input("Enter user name: ")
    email = input("Enter user email: ")
    try:
         user = Users.create(name, email)
         print(f'User created: {user}')
    except Exception as e:
        print(f'User not created: {e}')

def update_user():
        id = input("Enter user id: ")
        if user := Users.find_by_id(id):
            try:

                name = str( input("Enter user name: "))
                email = str(input("Enter user email: "))
                user.name = name
                user.email = email
                user.update()
                print(f'User updated: {user}')
            except Exception as e:
                print(f'User not updated: {e}')
        else:
            print("User not found")

def delete_user():
        id = input("Enter user id: ")
        if user := Users.find_by_id(id):
            user.delete()
            print(f'User deleted: {user}')
        else:
            print("User not found")

def list_users():
        for user in Users.get_all():
            print(user)

def list_jokes():
        for joke in Jokes.get_all():
            print(joke)

def find_joke_by_id():
        id = input("Enter joke id: ")
        joke = Jokes.find_by_id(id)
        print(joke) if joke else print ("Joke not found")

def find_joke_by_joke():
        joke = input("Enter joke: ")
        joke = Jokes.find_by_joke(joke)
        print(joke) if joke else print ("Joke not found")

def create_joke():
        user_id = input("Enter user id: ")
        joke = input("Enter joke: ")
        try:
            joke = Jokes.create(user_id, joke)
            print(f'Joke created: {joke}')
        except Exception as e:
            print(f'Joke not created: {e}')

def update_joke():
        id = input("Enter joke id: ")
        if joke := Jokes.find_by_id(id):
            try:
                user_id = input("Enter user id: ")
                joke.user_id = user_id
                joke.update()
                print(f'Joke updated: {joke}')
            except Exception as e:
                print(f'Joke not updated: {e}')
        else:
            print("Joke not found")

def delete_joke():
        id = input("Enter joke id: ")
        if joke := Jokes.find_by_id(id):
            joke.delete()
            print(f'Joke deleted: {joke}')
        else:
            print("Joke not found")

    
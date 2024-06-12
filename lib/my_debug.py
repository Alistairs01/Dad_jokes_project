from models.jokes import Jokes
from models.users import Users

def reset():
    Users.drop_table()
    Jokes.drop_table()
    Users.create_table()
    Jokes.create_table()
    user1 = Users.create("joe", "joe@me.com")
    user2 = Users.create("bob", "bob@me.com")
    joke1 = Jokes.create(user1.id, "Joke1")
    joke2 = Jokes.create(user2.id, "Joke2")
    

reset()
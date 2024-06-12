from models.__init__ import CONN, CURSOR
from models.users import Users

class Jokes:
    all = {}

    def __init__(self, joke, id=None, user_id = None):
        self.user_id = user_id
        self.joke = joke
        self.id = id

    def __repr__(self):
        return (
            f"<Jokes {self.joke} {self.id}>"

        )

    @property
    def joke(self):
        return self._joke

    @joke.setter
    def joke(self, joke):
        if isinstance(joke, str) and len(joke):
            self._joke = joke
        else:
            raise ValueError("Joke must be a non-empty string")

    @property
    def user_id(self):
        return self._user_id

    @user_id.setter
    def user_id(self, user_id):
        if type(user_id) is int and Users.find_by_id(user_id):
            self._user_id = user_id
        else:
            print("Invalid user id")

    @classmethod
    def create_table(cls):
        """Creates a new table to persist the attributes of Jokes instances"""
        sql = """
        CREATE TABLE IF NOT EXISTS jokes (
            id INTEGER PRIMARY KEY,
             joke TEXT,
            user_id INTEGER,
            FOREIGN KEY(user_id) REFERENCES users(id)
           
        )
        """
        CURSOR.execute(sql)
        CONN.commit()

    @classmethod
    def drop_table(cls):
        """Drops the table that persists Jokes instances"""
        sql = """
        DROP TABLE IF EXISTS jokes
        """
        CURSOR.execute(sql)
        CONN.commit()

    def  save(self):
        """
        Saves the Jokes instance to the database
        """
        sql = """
        INSERT INTO jokes (joke, user_id) VALUES (?, ?)
        """
        CURSOR.execute(sql, (self.joke, self.user_id))
        CONN.commit()
        self.id = CURSOR.lastrowid
        type(self).all[self.id] = self
    def update(self):
        """
        Updates the table row corresponding to the current joke
        """
        sql = """
        UPDATE jokes
        SET joke = ?
        WHERE id = ?
        """
        CURSOR.execute(sql, (self.joke, self.id))
        CONN.commit()
    def delete(self):
        """
        Deletes the table row corresponding to the current joke
        """
        sql = """
        DELETE FROM jokes
        WHERE id = ?
        """
        CURSOR.execute(sql, (self.id,))
        CONN.commit()
        del type(self).all[self.id]
        self.id = None
    @classmethod
    def create(cls, user_id, joke):
        """
        Creates a new joke and saves it to the database
        """
        joke = cls(user_id, joke)
        joke.save()
        return joke

    @classmethod
    def instance_from_db(cls, row):
        """"
        Returns a joke having the attribute values from the table row
        """
        joke = cls.all.get(row[0])

        if joke:
            joke.joke = row[1]
            joke.user_id = row[2]
        else:
            joke = cls(row[1], row[2])
            joke.id = row[0]
            cls.all[joke.id] = joke

        return joke
    @classmethod
    def get_all(cls):
        """
        Returns a list containing a joke object for each row in the table
        """
        sql = """
        SELECT * FROM jokes
        """
        CURSOR.execute(sql)
        rows = CURSOR.fetchall()
        return [cls.instance_from_db(row) for row in rows]
    @classmethod
    def find_by_id(cls, id):
        """
        Returns a joke having the given id
        """
        sql = """
        SELECT * FROM jokes
        WHERE id = ?
        """
        CURSOR.execute(sql, (id,))
        row = CURSOR.fetchone()
        return cls.instance_from_db(row) if row else None
    @classmethod
    def find_by_user_id(cls, user_id):
        """
        Returns a list of jokes created by the given user
        """
        sql = """
        SELECT * FROM jokes
        WHERE user_id = ?
        """
        CURSOR.execute(sql, (user_id,))
        rows = CURSOR.fetchall()
        return [cls.instance_from_db(row) for row in rows]
    
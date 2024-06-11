#lib/models/users.py
from models.__init__ import CONN, CURSOR


class Users:
    all = []
    def __init__(self, username, email, id=None):
        self.username = username
        self.email = email
        self.id = id
    def  __repr__(self):
        return f"<Users {self.username} {self.email} {self.id}>"
    @property
    def name(self):
        return self.username
    @name.setter
    def name(self, name):
        if isinstance(name, str) and len(name):
            self._name = name
        else:
            print("Name must be a non-empty string")

    @property
    def email(self):
        return self._email
    
    @email.setter
    def email(self, email):
        if isinstance(email, str) and len(email):
            self._email = email
        else:
            print("Email must be a non-empty string")

    @classmethod
    def create_table(cls):
        """
        Creates the table if it doesn't exist"""
        sql = """
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY,
            username TEXT,
            email TEXT
        )
        """
        CURSOR.execute(sql)
        CONN.commit()

    @classmethod
    def drop_table(cls):
        """
        Drops the table if it exists"""
        sql = """
        DROP TABLE IF EXISTS users
        """
        CURSOR.execute(sql)
        CONN.commit()
        
    def save(self):
        sql = """
        INSERT INTO users (username, email) VALUES (?, ?)
        """
        CURSOR.execute(sql, (self.username, self.email))
        CONN.commit()
        self.id = CURSOR.lastrowid
        type(self).all[self.id] = self

    @classmethod
    def create(cls, username, email):
        """
        Creates a new user and saves it to the database
        """
        user = cls(username, email)
        user.save()
        return user
    def update(self):
        """
        Updates the table row corresponding to the current user
        """
        sql = """
        UPDATE users
        SET username = ?, email = ?
        WHERE id = ?
        """
        CURSOR.execute(sql, (self.username, self.email, self.id))
        CONN.commit()
    def delete(self):
        """
        Deletes the table row corresponding to the current user
        """
        sql = """
        DELETE FROM users
        WHERE id = ?
        """
        CURSOR.execute(sql, (self.id,))
        CONN.commit()
        del type(self).all[self.id]
        self.id = None

    @classmethod
    def instance_from_db(cls, row):
        """
        Returns a user having the attribute values from the table row"""
        user = cls.all.get(row[0])

        if user:
            user.username = row[1]
            user.email = row[2]
        else:
            user = cls(row[1], row[2])
            user.id = row[0]
            cls.all[user.id]= user

        return user
    